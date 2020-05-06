"""
Given a set of candidate numbers (C) (without duplicates) and a target number
(T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


def combination_sum(candidates, target):
    result = set()
    candidates = [c for c in candidates if c <= target]

    for c in candidates:
        if c == target:
            result.add(tuple(c))


def test_combination_sum():
    assert combination_sum([2, 3, 6, 7], 7) == {(7, ), (2, 2, 3)}
