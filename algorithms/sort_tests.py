from unittest import TestCase


def quicksort(list_to_sort, start, end):
    """Operates in-place, memory efficient but unstable."""


class QuickSortTest(TestCase):

    def test_sort_in_place(self):
        l = [23, 98, 51, 11, 17, 88, 6, 30, 57]

        quicksort(l, start=0, end=len(l)-1)

        self.assertEqual([6, 11, 17, 23, 30, 51, 57, 88, 98], l)
