def frange(start, stop, step):
    pass


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
        pass


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


class LineHistory:
    pass


def skip_initial_lines(f):
    pass


def flatten(seq):
    pass


def gen_find_files(pattern):
    pass


def gen_opener(*filenames):
    pass


def gen_concatenate(*files):
    pass


def gen_grep(pattern):
    pass

