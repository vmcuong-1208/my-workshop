from pathlib import Path
import shutil
base = Path(r'b:/workshop/fcj-workshop-template/content/4-EventParticipated')
orig = base / '4.1-Event1'
if not orig.exists():
    raise SystemExit('Source folder not found: ' + str(orig))
copy_temp = base / '4.1-Event1-copy'
if copy_temp.exists():
    shutil.rmtree(copy_temp)
shutil.copytree(orig, copy_temp)
moves = [
    ('4.3-Event3', '4.4-Event4'),
    ('4.2-Event2', '4.3-Event3'),
    ('4.1-Event1', '4.2-Event2'),
]
for old_name, new_name in moves:
    old = base / old_name
    new = base / new_name
    if old.exists():
        if new.exists():
            raise SystemExit(f'Target exists: {new}')
        old.rename(new)
    else:
        print('Warning: missing', old)
new_copy = base / '4.1-Event1'
if new_copy.exists():
    raise SystemExit(f'New 4.1 dir already exists unexpectedly: {new_copy}')
copy_temp.rename(new_copy)
mapping = {
    '4.1-Event1': ('Event 1', '4.1.'),
    '4.2-Event2': ('Event 2', '4.2.'),
    '4.3-Event3': ('Event 3', '4.3.'),
    '4.4-Event4': ('Event 4', '4.4.'),
}
for folder, (title, pre) in mapping.items():
    idx = base / folder / '_index.md'
    if not idx.exists():
        print('Missing index in', folder)
        continue
    text = idx.read_text(encoding='utf-8')
    lines = text.splitlines()
    out = []
    for line in lines:
        if line.startswith('title: '):
            out.append(f'title: "{title}"')
        elif line.startswith('weight: '):
            out.append('weight: 1')
        elif line.startswith('pre: '):
            out.append(f'pre: " <b> {pre} </b> "')
        else:
            out.append(line)
    idx.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('Updated', idx)
print('Done')
