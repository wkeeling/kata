"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""
from collections import deque


def josephus(int_list, skip):
    skip = (skip - 1) * -1
    people = deque(int_list)

    while len(people) > 0:
        people.rotate(skip)
        yield people.popleft()


def josephus2(int_list, skip):
    skip = skip - 1                     # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip + idx) % len_list   # hash index to every 3rd
        yield int_list.pop(idx)
        len_list -= 1


def test_josephus():
    from timeit import timeit
    print('josephus: {}'.format(timeit('josephus([1, 2, 3, 4, 5, 6, 7, 8, 9], skip=3)', number=10000000, globals=globals())))
    print('josephus2: {}'.format(timeit('josephus2([1, 2, 3, 4, 5, 6, 7, 8, 9], skip=3)', number=10000000, globals=globals())))

    result = josephus([1, 2, 3, 4, 5, 6, 7, 8, 9], skip=3)

    assert list(result) == [3, 6, 9, 4, 8, 5, 2, 7, 1]
