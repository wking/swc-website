#!/usr/bin/python3.3

import codecs as _codecs
import json as _json


def get_metadata(s):
    lines = s.splitlines(True)
    metadata = {}
    while lines and lines[0].strip():
        line = lines.pop(0)
        try:
            key,value = line.split(':', 1)
        except ValueError as e:
            raise ValueError(line) from e
        metadata[key.strip().lower()] = value.strip()
    if lines and not lines[0].strip():
        lines.pop(0)
    return metadata, ''.join(lines)

def convert(source, target):
    with _codecs.open(source, 'r', 'utf-8') as f:
        s = f.read()
    meta,body = get_metadata(s)
    with _codecs.open(target, 'w', 'utf-8') as f:
        f.write('\n'.join([
                    '---',
                    _json.dumps(meta, indent=2),
                    '---',
                    body]))


if __name__ == '__main__':
    import sys

    for path in sys.argv[1:]:
        target = path.replace('.md', '.jinja')
        convert(path, target)
