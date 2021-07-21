from collections import deque
from itertools import groupby


class World:
    def __init__(self, val):
        self.val = val

    # def __iter__(self):
    #     return iter(self.val)

    def __getitem__(self, item):
        return self.val[item]


def search(f, search_string, history=10):
    history = deque(maxlen=history)
    for line in f:
        line = line.strip()
        if search_string in line:
            yield line, list(history)
        history.append(line)

import heapq


class PriorityQueue:

    def __init__(self):
        self.q = []
        self.index = 0

    def push(self, item, priority):
        self.q.append((-priority, self.index, item))
        self.index += 1
        heapq.heapify(self.q)

    def pop(self):
        print(self.q)
        return self.q.pop(0)


def dedupe(seq, key=None):
    seen = set()
    for v in seq:
        v1 = v if key is None else key(v)
        if v1 not in seen:
            yield v
        seen.add(v)


def group_by_date(rows):
    rows = sorted(rows, key=lambda x: x['date'])
    ret = {}
    for k, grp in groupby(rows, key=lambda x: x['date']):
        ret[k] = list(grp)
    return ret