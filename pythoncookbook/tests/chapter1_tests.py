"""Chapter 1: Data Structures and Algorithms."""

from statistics import mean
from unittest import TestCase

from pythoncookbook.code.chapter1 import (search,
                                          World)


class UnpackingSequenceTest(TestCase):

    def test_unpack_sequence(self):
        self.fail('Write a single line variable assignment')

        self.assertEquals(name, 'ACME')
        self.assertEquals(shares, 50)
        self.assertEquals(price, 91.1)
        self.assertEquals(date, (2012, 12, 21))

    def test_unpack_sequence_nested_tuple(self):
        self.fail('Write a single line variable assignment')

        self.assertEquals(name, 'ACME')
        self.assertEquals(shares, 50)
        self.assertEquals(price, 91.1)
        self.assertEquals(year, 2012)
        self.assertEquals(year, 12)
        self.assertEquals(year, 21)

    def test_unpack_sequence_string(self):
        self.fail('Write a single line variable assignment')

        self.assertEquals(a, 'H')
        self.assertEquals(b, 'e')
        self.assertEquals(c, 'l')
        self.assertEquals(d, 'l')
        self.assertEquals(e, 'o')

    def test_unpack_sequence_object(self):
        a, b, c, d, e = World

        self.assertEquals(a, 'W')
        self.assertEquals(b, 'o')
        self.assertEquals(c, 'r')
        self.assertEquals(d, 'l')
        self.assertEquals(e, 'd')


class UnpackingElementsFromIterablesArbitraryLengthTest(TestCase):

    def test_drop_first_last(self):
        grades = [56, 77, 75, 68, 53, 62, 44]

        self.fail('Write a single line variable assignment')

        self.assertEquals(first, 56)
        self.assertEquals(mean(middle), 67)
        self.assertEquals(last, 44)

    def test_unpack_phone_numbers(self):
        record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

        self.fail('Write a single line variable assignment')

        self.assertEquals(name, 'Dave')
        self.assertEquals(email, 'dave@example.com')
        self.assertEquals(phone_numbers, ['773-555-1212', '847-555-1212'])

    def test_unpack_last(self):
        values = [5, 8, 3, 1, 9]

        self.fail('Write a single line variable assignment')

        self.assertEquals(mean(first_four), 4.25)
        self.assertEquals(last, 9)

    def test_iterate_varying_length_tuples(self):
        records = [
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4),
        ]

        def do_foo(x, y):
            print('foo', x, y)

        def do_bar(s):
            print('bar', s)

        self.fail('Iterate records calling appropriate function')

    def test_unpack_split_string(self):
        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

        self.fail('Write a single line variable assignment')

        self.assertEqual(uname, 'nobody')
        self.assertEqual(homedir, '/var/empty')
        self.assertEqual(sh, '/usr/bin/false')


class KeepingTheLastNItemsTest(TestCase):

    def test_find_lines_with_history(self):
        """Hint: the search function can be implemented as a generator.
        Think about the data structure used to keep track of the history.
        """
        found = {}
        with open('data/find_lines_with_history.txt') as f:
            for line, prevlines in search(f, 'python', history=5):
                found[line] = prevlines
                for pline in prevlines:
                    print(pline)
                print(line)

        self.assertEqual(len(found), 2)
        self.assertEqual(found['line8 python'],
                         ['line3', 'line4', 'line5', 'line6', 'line7'])
        self.assertEqual(found['line14 python'],
                         ['line9', 'line10', 'line11', 'line12', 'line13'])


class FindingTheLargestOrSmallestNItemsTest(TestCase):

    def test_find_three_largest_items(self):
        """Hint: do this without using slice syntax."""
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

        self.fail('Write a single line variable assignment')

        self.assertEqual(largest, [42, 37, 23])

    def test_find_three_smallest_items(self):
        """Hint: do this without using slice syntax and do not
        sort the list.
        """
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

        self.fail('Write a single line variable assignment')

        self.assertEqual(smallest, [-4, 1, 2])

    def test_find_three_largest_items_complex(self):
        portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]

        self.fail('Write a single line variable assignment')

        self.assertEqual(expensive, [200, 100, 75])