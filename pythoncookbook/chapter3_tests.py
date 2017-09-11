"""Chapter 3: Numbers, Dates and Times."""

from fractions import Fraction
import math
from unittest import TestCase


class RoundingNumericalValuesTest(TestCase):

    def test_round_floating_point_number(self):
        num = 1.23

        self.fail('Write a single line expression')

        self.assertEqual(rounded, 1.2)

    def test_round_nearest_even(self):
        """Hint: use the same mechanism, but observe how
        the result is rounded to the nearest even number.
        """
        a = 1.5
        b = 2.5

        self.fail('Round the two numbers')

        self.assertEqual(a_rounded, 2)
        self.assertEqual(b_rounded, 2)

    def test_round_tens(self):
        a = 1627731

        self.fail('Write a single line expression')

        self.assertEqual(rounded, 1627730)

    def test_round_hundreds(self):
        a = 1627731

        self.fail('Write a single line expression')

        self.assertEqual(rounded, 1627700)

    def test_round_thousands(self):
        a = 1627731

        self.fail('Write a single line expression')

        self.assertEqual(rounded, 1628000)

    def test_format_two_decimal_places(self):
        """Hint: don't use round when formatting text."""
        x = 1.23456

        self.fail('Write a single line expression')

        self.assertEqual(formatted, '1.23')


class PerformingAccurateDecimalCalculations(TestCase):

    def test_perform_accurate_calculation(self):
        """Hint: add the variables together but note that adding
        them as floats will not give the desired result due to
        floating point inaccuracies.
        """
        a = 4.2
        b = 2.1

        self.fail('Write a single line expression')

        self.assertEqual(c, '6.3')


class FormattingNumbersForOutput(TestCase):

    def setUp(self):
        self._x = 1234.56789

    def test_format_two_decimal_places(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '1234.57')

    def test_format_right_justified_10_chars_one_decimal_place(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '    1234.6')

    def test_format_left_justified_10_chars_one_decimal_place(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '1234.6    ')

    def test_format_one_decimal_place_include_thousands_sep(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '1,234.6')


class WorkingWithInfinityAndNaNsTest(TestCase):

    def test_create_infinity_value(self):
        self.fail('Write a single line expression')

        self.assertTrue(math.isinf(x))

    def test_create_nan_value(self):
        self.fail('Write a single line expression')

        self.assertTrue(math.isnan(x))


class CalculatingWithFractionsTest(TestCase):

    def test_add_fractions(self):
        a = 0
        b = 0

        self.assertEqual(a + b, Fraction(27, 16))


class PickingThingsAtRandomTest(TestCase):
    pass