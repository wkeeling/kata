"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]
"""
from collections import deque
import timeit


def move_zeros(arr):
    ret = [v for v in arr if v is False or v != 0]
    ret += [0] * (len(arr) - len(ret))
    return ret


def move_zeros_deque(arr):
    ret = deque([v for v in arr if v is False or v != 0])
    for i in range(len(arr) - len(ret)):
        ret.insert(len(ret) - 1, 0)
    return ret


def test_move_zeros():
    t = timeit.timeit('move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])',
                      globals=globals(), number=10000000)
    print('move_zeros(): {}'.format(t))
    # t1 = timeit.timeit('move_zeros_deque([False, 1, 0, 1, 2, 0, 1, 3, "a"])',
    #                   globals=globals(), number=10000000)
    # print('move_zeros_deque(): {}'.format(t1))
    assert move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]) == \
           [False, 1, 1, 2, 1, 3, "a", 0, 0]


