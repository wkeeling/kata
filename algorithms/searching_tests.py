from unittest import TestCase


def find_integer_position(l, i):
    return None


class SearchingTest(TestCase):

    def test_find_integer(self):
        l = [23, 98, 51, 11, 17, 88, 6, 30, 57]

        self.assertEqual(find_integer_position(l, 30), 4)

    def test_find_integer_duplicate(self):
        l = [23, 98, 42, 30, 51, 11, 17, 88, 6, 30, 57]

        self.assertEqual(find_integer_position(l, 30), 4)

    def test_find_integer_even_list(self):
        l = [23, 98, 42, 30, 51, 11, 17, 88]

        self.assertEqual(find_integer_position(l, 30), 4)
