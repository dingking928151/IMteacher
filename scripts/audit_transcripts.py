"""Inspect local watch evidence without downloading or changing media."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'research' / 'claude'
stamp = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})')

def seconds(s):
    h, m, sec = s.split(':')
    return int(h) * 3600 + int(m) * 60 + float(sec)

for folder in sorted(root.glob('*_work')):
    download = folder / 'download'
    path = download / 'video.en.vtt'
    meta = download / 'video.info.json'
    if not path.exists() or not meta.exists():
        print(json.dumps({'folder': str(folder), 'status': 'incomplete'}, ensure_ascii=False))
        continue
    data = json.loads(meta.read_text(encoding='utf-8-sig'))
    text = path.read_text(encoding='utf-8-sig')
    spans = stamp.findall(text)
    print(json.dumps({
        'title': data.get('title'), 'id': data.get('id'),
        'uploader': data.get('uploader'), 'duration': data.get('duration'),
        'subtitle_file': str(path), 'bytes': path.stat().st_size,
        'cues': len(spans), 'start': spans[0][0] if spans else None,
        'end': spans[-1][1] if spans else None,
        'span_seconds': round(seconds(spans[-1][1])-seconds(spans[0][0]), 3) if spans else 0,
        'note': 'A timestamp span does not prove gap-free content or visual inspection.'
    }, ensure_ascii=False))
