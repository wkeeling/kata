"""
Find the index of 0 to be replaced with 1 to get
longest continuous sequence
of 1s in a binary array.
Returns index of 0 to be
replaced with 1 to get longest
continuous sequence of 1s.
If there is no 0 in array, then
it returns -1.
e.g.
let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
"""


def max_ones_index(arr):
    pass


def test_max_ones_index():
    assert max_ones_index([1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]) == 3
