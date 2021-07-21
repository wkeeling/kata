from collections import deque
from functools import partial
from itertools import dropwhile


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self._children:
            yield from c.depth_first()


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


class LineHistory:

    def __init__(self, f):
        self.history = deque(maxlen=3)
        self.f = f

    def __iter__(self):
        for i, line in enumerate(self.f):
            line = line.strip()
            yield line
            self.history.append((i+1, line))


def skip_initial_lines(filename):
    with open(filename) as f:
        yield from dropwhile(lambda l: l.startswith('#'), f)


def flatten(seq):
    for x in seq:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x

from fnmatch import fnmatch


def gen_find_files(pattern):
    for f in fnmatch('data', pattern):
        yield f


def gen_opener(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield f


def gen_concatenate(files):
    concat = ''
    for f in files:
        concat += f.read()



def gen_grep(pattern, lines):
    pass

