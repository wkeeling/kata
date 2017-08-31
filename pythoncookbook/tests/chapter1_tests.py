"""Chapter 1: Data Structures and Algorithms."""

from statistics import mean
from unittest import TestCase

from pythoncookbook.code.chapter1 import World


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


class UnpackElementsFromIterablesArbitraryLengthTest(TestCase):

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