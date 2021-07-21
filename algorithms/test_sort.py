import cProfile
import itertools
import random
from timeit import timeit


def quicksort(lst, start, end):
    """Quicksort over a list-like sequence"""
    if start >= end:
        return
    low, high = start, end
    pivot = lst[start + (end - start) // 2]

    while low <= high:
        while lst[low] < pivot:
            low += 1
        while lst[high] > pivot:
            high -= 1
        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
            low, high = low + 1, high - 1

    quicksort(lst, low, end)
    quicksort(lst, start, high)


def bubblesort(lst):
    for _ in range(len(lst)):  # Don't care about the outer loop var
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

x = list(range(20))
random.shuffle(x)


def test_quicksort():
    import random
    lst = list(range(20))
    random.shuffle(lst)
    print(lst)
    bubblesort(lst)
    print(lst)

    # print('Sorting {}'.format(x))
    # cProfile.runctx('quicksort(x)', globals=globals(), locals=locals())
    # s = quicksort(x)
    # # print(list(s))
    # print(timeit('quicksort(x)', globals=globals()))
    # print(timeit('bubblsort(x)', globals=globals()))

if __name__ == '__main__':
    test_quicksort()
