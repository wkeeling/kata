"""
WAP to take one element from each of the array add it to the target sum.
Print all those three-element combinations.
/*
A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [2, 3, 3, 4]
target = 7
*/
Result:
[[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 4, 2],
 [2, 2, 3], [2, 2, 3], [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
"""
from itertools import product
from timeit import timeit


def array_sum_combinations(a, b, c, target):
    result = []

    for x in a:
        for y in b:
            for z in c:
                if x + y + z == target:
                    result.append([x, y, z])

    return result


def array_sum_combinations2(a, b, c, target):
    return [list(p) for p in product(a, b, c) if sum(p) == target]


def test_array_sum_combinations():
    a = [1, 2, 3, 3]
    b = [2, 3, 3, 4]
    c = [2, 3, 3, 4]
    target = 7

    print(timeit('a=[1, 2, 3, 3];b=[2, 3, 3, 4];c=[2, 3, 3, 4];target=7;array_sum_combinations(a, b, c, target)', globals=globals()))
    result = array_sum_combinations2(a, b, c, target)

    # assert result == [[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 4, 2],
    #                   [2, 2, 3], [2, 2, 3], [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
