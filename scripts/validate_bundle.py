"""Validate package metadata, local reference integrity and shared-contract drift."""
from pathlib import Path
import re
import sys
import yaml

root = Path(__file__).resolve().parents[1]
expected = {'using-im', 'implanner', 'imteacher', 'imsupervisor', 'imreflect', 'imcompanion', 'imwork', 'imcowork'}
errors = []
actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
if actual != expected:
    errors.append(f'Skill set differs: {actual ^ expected}')
shared_files = ('state-contract.md', 'adaptation-loop.md', 'onboarding.md', 'agent-runtime.md', 'feedback-loop.md', 'background-followups.md')
for name in sorted(expected):
    folder = root / 'skills' / name
    main = folder / 'SKILL.md'
    if not main.exists():
        errors.append(f'Missing: {main}')
        continue
    text = main.read_text(encoding='utf-8-sig')
    parts = text.split('---', 2)
    try:
        data = yaml.safe_load(parts[1])
        if data.get('name') != name or not data.get('description', '').startswith('Use when'):
            errors.append(f'Invalid discovery metadata: {name}')
    except (IndexError, AttributeError, yaml.YAMLError) as e:
        errors.append(f'Frontmatter: {name}: {e}')
    for shared_name in shared_files:
        reference = folder / 'references' / shared_name
        if not reference.exists() or reference.read_bytes() != (root / 'shared' / shared_name).read_bytes():
            errors.append(f'Shared reference drift: {name}/{shared_name}')
    for md in folder.rglob('*.md'):
        content = md.read_text(encoding='utf-8-sig')
        links = re.findall(r'\]\(([^)]+)\)', content)
        code_refs = re.findall(r'`(references/[^`]+\.md)`', content)
        for link in links + code_refs:
            if re.match(r'^[a-z]+://', link) or link.startswith('#'):
                continue
            path = link.split('#')[0]
            if not (md.parent / path).exists():
                # Legacy main-file code references are relative to the skill root.
                if not (folder / path).exists():
                    errors.append(f'Broken reference: {md.relative_to(root)} -> {link}')
    print(f'CHECKED {name}: metadata, references, shared contract')

original_refs = {'checkpoint-bank.md', 'code-three-stage.md', 'hands-on-mode.md',
                 'learner-profile.md', 'multi-line-review.md', 'quiz-and-review.md',
                 'record-keeping.md', 'teaching-loop.md'}
present = {p.name for p in (root / 'skills/imteacher/references').glob('*.md')}
if not original_refs <= present:
    errors.append(f'Lost legacy teacher references: {original_refs - present}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('PASS: all eight skills; structural checks only, not behavioral validation.')
