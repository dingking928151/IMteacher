"""Build and verify a rules-only portable bundle, excluding research and user state."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--version', required=True, choices=['0.4', '0.5', '0.6', '0.7'])
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
members = {}
for base in ('skills', 'shared', 'adapters/personal-agent'):
    for p in sorted((root / base).rglob('*.md')):
        if p.is_symlink() or not p.resolve().is_relative_to((root / base).resolve()):
            raise SystemExit(f'External/symlink member rejected: {p}')
        members[p.relative_to(root).as_posix()] = p.read_bytes()
if not members:
    raise SystemExit('No source files')
package = root / 'dist' / f'im-skills-agent-v{args.version}.zip'
package.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(package, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, data in members.items():
        z.writestr(name, data)
with zipfile.ZipFile(package) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(members)
    assert set(z.namelist()) == set(members)
    for name, data in members.items():
        assert z.read(name) == data, name
report = {'version': args.version, 'files': len(members),
          'sha256': hashlib.sha256(package.read_bytes()).hexdigest(),
          'members': list(members)}
out = root / 'tests' / ('round' + args.version.rsplit('.', 1)[1]) / 'package.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'PASS: {len(members)} whitelist Markdown members verified; SHA256 {report["sha256"]}')
