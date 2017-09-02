"""Chapter 1: Data Structures and Algorithms."""

from statistics import mean
from unittest import TestCase

from pythoncookbook.code.chapter1 import (dedupe,
                                          PriorityQueue,
                                          search,
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
        """Hint: do this without using slice syntax and do not
         sort the list.
         """
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


class ImplementingAPriorityQueueTest(TestCase):

    def test_should_get_items_with_highest_priority(self):
        """Hint: PriorityQueue should negate the priority when it
        pushes the item. The items are stored in a tuple in the queue."""
        class Item:
            def __init__(self, name):
                self.name = name

            def __repr__(self):
                return 'Item({!r})'.format(self.name)

        q = PriorityQueue()
        q.push(Item('foo'), 1)
        q.push(Item('bar'), 5)
        q.push(Item('spam'), 4)
        q.push(Item('grok'), 1)

        self.assertEqual(q.pop().name, 'bar')
        self.assertEqual(q.pop().name, 'spam')
        self.assertEqual(q.pop().name, 'foo')
        self.assertEqual(q.pop().name, 'grok')


class MappingKeysToMutipleValuesDictionaryTest(TestCase):

    def test_append_to_list_value(self):
        self.fail('Write a single line variable assignment')

        try:
            d['a'].append(1)
            d['a'].append(2)
            d['b'].append(4)
        except KeyError:
            pass  # Should not raise


class CalculatingWithDictionariesTest(TestCase):

    def setUp(self):
        self._prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }

    def test_find_min_price(self):
        self.fail('Write a single line variable assignment')

        self.assertEqual(min_price, (10.75, 'FB'))

    def test_find_max_price(self):
        self.fail('Write a single line variable assignment')

        self.assertEqual(max_price, (612.78, 'AAPL'))

    def test_sort_prices(self):
        self.fail('Write a single line variable assignment')

        self.assertEqual(prices_sorted, [(10.75, 'FB'), (37.2, 'HPQ'),
                                         (45.23, 'ACME'), (205.55, 'IBM'),
                                         (612.78, 'AAPL')])

    def test_raises_value_error(self):
        self.fail('Write a single line variable assignment')

        with self.assertRaises(ValueError):
            min(prices_and_names)
            max(prices_and_names)


class FindingCommonalitiesInTwoDictionariesTest(TestCase):

    def setUp(self):
        self._a = {
            'x': 1,
            'y': 2,
            'z': 3
        }
        self._b = {
            'w': 10,
            'x': 11,
            'y': 2
        }

    def test_find_keys_in_common(self):
        self.fail('Write a single line variable assignment')

        self.assertEqual(common_keys, {'x', 'y'})

    def test_find_keys_in_a_not_b(self):
        """Hint: think of it as removing b's keys from a."""
        self.fail('Write a single line variable assignment')

        self.assertEqual(keys, {'z'})

    def test_find_key_value_pairs_in_common(self):
        self.fail('Write a single line variable assignment')

        self.assertEqual(common_pairs, {('y', 2)})


class RemovingDuplicatesFromASequencePreservingOrderTest(TestCase):

    def test_dedupe_sequence(self):
        """Hint: dedupe() could also be used to de-dupe any type of iterable,
        not just a list."""
        a = [1, 5, 2, 1, 9, 1, 5, 10]

        b = list(dedupe(a))

        self.assertListEqual(b, [1, 5, 2, 9, 10])

    def test_dedupe_sequence_hashable_items(self):
        a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2},
             {'x': 2, 'y': 4}]

        b = list(dedupe(a, key=lambda d: (d['x'], d['y'])))

        self.assertListEqual(b, [{'x': 1, 'y': 2}, {'x': 1, 'y': 3},
                                 {'x': 2, 'y': 4}])

        b = list(dedupe(a, key=lambda d: d['x']))

        self.assertListEqual(b, [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}])


class NamingASliceTest(TestCase):

    def test_use_named_slice(self):
        record = '....................100          .......513.25     ........'

        self.fail('Retrive the information from the string')

        self.assertEquals(shares, 100)
        self.assertEqual(price, 513.25)


class DeterminingMostFrequentlyOccurringItemsInASequenceTest(TestCase):

    pass