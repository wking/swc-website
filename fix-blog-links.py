#!/usr/bin/python3.3

import glob as _glob
import os as _os
import re as _re


LINK_REGEXP = _re.compile('\|filename\|/blog/(\d+)/(\d+)/([^.]+).html')


class Replacer (object):
    def __init__(self, path):
        self.path = path

    def __call__(self, match):
        glob = _os.path.join(
            _os.path.dirname(path),
            '{}-{}-*-{}.md'.format(
                match.group(1), match.group(2), match.group(3)))
        matches = _glob.glob(glob)
        assert len(matches) == 1, (glob, matches)
        filename = _os.path.basename(matches[0])
        return '|filename|{}'.format(filename)

def convert(path):
    with open(path, 'r') as f:
        s = f.read()
    t = LINK_REGEXP.sub(Replacer(path), s)
    with open(path, 'w') as f:
        f.write(t)


if __name__ == '__main__':
    import sys

    for path in sys.argv[1:]:
        convert(path)
