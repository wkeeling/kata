"""
Given two strings, determine if they are equal after reordering.
Examples:
"apple", "pleap"  -> True
"apple", "cherry" -> False
"""

from collections import Counter, defaultdict
import timeit


def is_equal1(str1, str2):
    return Counter(str1) == Counter(str2)


def is_equal2(str1, str2):
    d1, d2 = defaultdict(int), defaultdict(int)

    for c in str1:
        d1[c] += 1

    for c in str2:
        d2[c] += 1

    return d1 == d2


def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for c in s1:
        pos = ord(c)-ord('a')
        c1[pos] = c1[pos] + 1

    for c in s2:
        pos = ord(c)-ord('a')
        c2[pos] = c2[pos] + 1

    return c1 == c2


def test_anagram():
    print('is_equal1: {}'.format(
        timeit.timeit("is_equal1('apple', 'pleap')", globals=globals())))
    print('is_equal2: {}'.format(
        timeit.timeit("is_equal2('apple', 'pleap')", globals=globals())))
    print('anagram: {}'.format(
        timeit.timeit("anagram('apple', 'pleap')", globals=globals())))
    # assert is_equal2('apple', 'pleap')
    # assert not is_equal2('apple', 'cherry')
