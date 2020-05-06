from collections import deque


def slice_deque(d, start, stop):
    d.rotate(-start)
    s = deque()
    for _ in range(stop - start):
        s.append(d[0])
        d.rotate(-1)
    d.rotate(stop)
    return s
