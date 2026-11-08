"""Smoke test the release's portable follow-up entry points and file allowlist."""
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'background-followups.md'


def main():
    contract = ROOT / 'shared' / NAME
    assert contract.is_file(), 'Missing shared background follow-up contract'
    for skill in sorted((ROOT / 'skills').iterdir()):
        if not skill.is_dir():
            continue
        reference = skill / 'references' / NAME
        assert reference.read_bytes() == contract.read_bytes(), f'{skill.name}: reference drift'
        entry = (skill / 'SKILL.md').read_text(encoding='utf-8-sig')
        assert f'(references/{NAME})' in entry, f'{skill.name}: detached workflow'
    if len(sys.argv) == 2:
        with zipfile.ZipFile(sys.argv[1]) as package:
            names = set(package.namelist())
            allowed = {'shared', 'skills', 'adapters/personal-agent'}
            expected = {p.relative_to(ROOT).as_posix() for base in allowed
                        for p in (ROOT / base).rglob('*.md')}
            assert names == expected, 'Package omitted a rule or included files outside the allowlist'
            assert package.read(f'shared/{NAME}') == contract.read_bytes(), 'Stale ZIP reference'
    print('PASS: background follow-up entry points and portable references')


if __name__ == '__main__':
    main()
