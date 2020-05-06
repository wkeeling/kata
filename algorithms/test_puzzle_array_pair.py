from unittest import TestCase


def find_pairs(a, s):
    vals = {i for i in a}
    pairs = []

    for i in a:
        rem = s - i
        if rem in vals:
            pairs.append((i, rem))
            vals.remove(rem)

    return pairs


class PuzzleArrayPairTest(TestCase):

    def test_find_pairs(self):
        a = [1, 5, 7, -1, 5]
        s = 6

        self.assertEqual([(1, 5), (7, -1), (1, 5)], find_pairs(a, s))
