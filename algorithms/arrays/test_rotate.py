"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""
from collections import deque


def rotate1(arr, steps):
    arr = list(arr)
    for _ in range(steps):
        arr.insert(0, arr.pop(len(arr) - 1))
    return arr


def rotate2(arr, steps):
    d = deque(arr)
    d.rotate(steps)
    return list(d)


def rotate3(arr, steps):
    return arr[-steps:] + arr[:-steps]


def test_rotate():
    arr = [1, 2, 3, 4, 5, 6, 7]

    assert rotate1(arr, 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate2(arr, 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate3(arr, 3) == [5, 6, 7, 1, 2, 3, 4]
