from unittest import TestCase


def find_position(val, search_list):
    """Runs in O(log n) time, O(1) space. Always finds leftmost element."""
    start, end = 0, len(search_list)

    while start <= end:
        mid = (start + end) // 2

        if search_list[mid] < val:
            start = mid + 1
        elif search_list[mid] > val:
            end = mid - 1
        else:
            return mid


class BinarySearchTest(TestCase):
    """Remember to you need to do something to each list before
    it can be searched.
    """

    def test_find_integer(self):
        l = sorted([23, 98, 51, 11, 17, 88, 6, 30, 57])

        self.assertEqual(7, find_position(88, l))

    def test_find_integer_duplicate(self):
        l = sorted([23, 98, 42, 30, 51, 11, 17, 88, 6, 30, 57])

        self.assertEqual(5, find_position(30, l))

    def test_find_integer_even_list(self):
        l = sorted([23, 98, 42, 30, 51, 11, 17, 88])

        self.assertEqual(3, find_position(30, l))

    def test_find_float(self):
        l = sorted([23.8, 98, 42.5, 30.4, 51, 11, 17.9, 88])

        self.assertEqual(3, find_position(30.4, l))

    def test_no_match(self):
        l = sorted([23, 98, 51, 11, 17, 88, 6, 30, 57])

        self.assertIsNone(find_position(99, l))
