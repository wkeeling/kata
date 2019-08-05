"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]
"""


def delete_nth(arr, n):
    return []


def test_delete_nth():
    n = 2
    arr = [1, 2, 3, 1, 2, 1, 2, 3]

    result = delete_nth(arr, n)

    assert result == [1, 2, 3, 1, 2, 3]
