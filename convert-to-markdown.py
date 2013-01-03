#!/usr/bin/python3.3

import collections as _collections
import re as _re


METADATA_REGEXP = _re.compile('<meta name="([^"]*)" content="([^"]*)" />')

def get_metadata(text):
    meta = _collections.OrderedDict()
    for key,value in METADATA_REGEXP.findall(text):
        if key in meta:
            meta[key].append(value)
        else:
            meta[key] = [value]
    meta['tags'] = meta.pop('category')
    return meta

def get_content(text):
    lines = []
    in_content = False
    for line in text.splitlines():
        if line == '{% endblock content %}':
            in_content = False
        if in_content:
            lines.append(line)
        if line == '{% block content %}':
            in_content = True
    return '\n'.join(lines)

def convert(source, target):
    with open(source, 'r') as f:
        s = f.read()
    meta = get_metadata(s)
    chunks = []
    # For ReST.  Markdown uses metadata for titles
    #chunks.extend([meta['title'][0], '#'*len(meta['title'][0]), ''])
    #meta.pop('title')
    for key,value in meta.items():
        key = key.title()
        if len(value):
            chunks.append('{}: {}'.format(key, ', '.join(value)))
        else:
            chunks.append('{}: {}'.format(key, value[0]))
    chunks.append('')
    chunks.extend([get_content(s), ''])

    with open(target, 'w') as f:
        f.write('\n'.join(chunks))


if __name__ == '__main__':
    import sys

    for path in sys.argv[1:]:
        target = path.replace('.html', '.md')
        convert(path, target)
