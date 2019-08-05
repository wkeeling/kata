
"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


def longest_non_repeat(string):
    pass


def test_longest_non_repeat():
    assert longest_non_repeat('abcabcbb') == 'abc'
    assert longest_non_repeat('bbbbb') == 'b'
    assert longest_non_repeat('pwwkew') == 'wke'

