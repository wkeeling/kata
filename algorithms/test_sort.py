import cProfile
import itertools
import random
from timeit import timeit


def quicksort(lst):
    """Quicksort over a list-like sequence"""
    if len(lst) == 0:
        # print('Exiting with []')
        return lst

    pivot = lst[0]
    pivots = [x for x in lst if x == pivot]

    # print('Sorting small {} (lst is {}, pivot is {})'.format([x for x in lst if x < pivot],
    # lst, pivot))
    small = quicksort([x for x in lst if x < pivot])
    # print('Sorting large {} (lst is {}, pivot is {})'.format([x for x in lst if x > pivot],
    # lst, pivot))
    large = quicksort([x for x in lst if x > pivot])

    # print('Exiting with {}'.format(small + pivots + large))
    return small + pivots + large


def bubblesort(lst):
    for j in range(len(lst)):
        for k in range(len(lst) - 1):
            if lst[k] > lst[k + 1]:
                lst[k], lst[k + 1] = lst[k + 1], lst[k]


x = list(range(20))
random.shuffle(x)


def test_quicksort():
    # print('Sorting {}'.format(x))
    # cProfile.runctx('quicksort(x)', globals=globals(), locals=locals())
    # s = quicksort(x)
    # print(list(s))
    print(timeit('quicksort(x)', globals=globals()))
    print(timeit('bubblsort(x)', globals=globals()))
