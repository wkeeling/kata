"""Chapter 3: Numbers, Dates and Times."""

from datetime import (datetime,
                      timedelta)
from fractions import Fraction
import math
from unittest import TestCase

from pythoncookbook.chapter3 import (date_range,
                                     get_days_in_month)


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

    def test_divide_a_by_b_and_round_to_3_decimal_places(self):
        """Hint: don't use floats, and don't use round()."""
        a = 1.3
        b = 1.7

        self.fail('Do the calculation and round the result')

        self.assertEqual(c, '0.765')


class FormattingNumbersForOutput(TestCase):

    def setUp(self):
        self._x = 1234.56789

    def test_format_two_decimal_places(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '1234.57')

    def test_format_right_justified_10_chars_one_decimal_place(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '    1234.6')

    def test_format_left_justified_10_chars_three_decimal_places(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '1234.678  ')

    def test_format_center_justified_10_chars_one_decimal_place(self):
        self.fail('Write a single line expression')

        self.assertEqual(formatted, '  1234.6  ')

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

    def test_pick_random_item_from_sequence(self):
        values = [1, 2, 3, 4, 5, 6]

        self.fail('Write a single line expression')

        self.assertIn(val, values)

    def test_pick_two_random_items_from_sequence(self):
        values = [1, 2, 3, 4, 5, 6]

        self.fail('Write a single line expression')

        self.assertEqual(len(vals), 2)
        for val in vals:
            self.assertIn(val, values)

    def test_shuffle_sequence(self):
        values = [1, 2, 3, 4, 5, 6]

        self.fail('Create a new list based on shuffling values')

        self.assertNotEqual(shuffled, values)

    def test_create_random_integer_between_1_and_10(self):
        self.fail('Write a single line expression')

        self.assertIn(i, range(1, 10))

    def test_create_random_float_between_0_and_1(self):
        self.fail('Write a single line expression')

        self.assertGreaterEqual(i, 0)
        self.assertLessEqual(i, 1)


class ConvertingDaysToSecondsAndOtherBasicTimeConversions(TestCase):

    def test_arithmetic_with_units_of_time(self):
        self.fail('Define three variables, the third should be the '
                  'sum of the first two')

        self.assertEqual(a.days, 2)
        self.assertEqual(b.days, 3)
        self.assertEqual(c.days, 5)

    def test_arithmetic_with_units_of_time_2(self):
        self.fail('Define three variables, the third should be the '
                  'result of dividing the first by the second.')

        self.assertEqual(a.days, 4)
        self.assertEqual(b.days, 2)
        self.assertEqual(c, 2.0)

    def test_arithmetic_with_specific_dates(self):
        a = datetime(2012, 9, 23)
        b = datetime(2012, 12, 21)

        self.fail('Write a single line expression')

        self.assertEqual(c.days, 89)

    def test_relative_time_between_two_dates(self):
        """Hint: this uses a 3rd party package."""
        a = datetime(2012, 9, 23)
        b = datetime(2012, 12, 21)

        self.fail('Write a single line expression')

        self.assertEqual(d.months, 2)
        self.assertEqual(d.days, 28)


class DeterminingLastFridaysDate(TestCase):

    def test_find_last_friday(self):
        """Hint: this uses a 3rd party package."""
        d = datetime(2017, 9, 16, 10, 0, 0, 0)

        self.fail('Write a single line expression')

        self.assertEqual(last_friday, datetime(2017, 9, 15, 10, 0, 0, 0))

    def test_find_next_friday(self):
        """Hint: this uses a 3rd party package."""
        d = datetime(2017, 9, 16, 10, 0, 0, 0)

        self.fail('Write a single line expression')

        self.assertEqual(next_friday, datetime(2017, 9, 22, 10, 0, 0, 0))


class FindingTheDateRangeForTheCurrentMonth(TestCase):

    def test_iterate_days_in_month(self):
        """Hint: use the calendar module to get the number of days in
        the month.
        """
        days = list(get_days_in_month(datetime(2017, 9, 16, 0, 0, 0, 0)))

        self.assertEqual(len(days), 30)
        self.assertEqual(days[0], datetime(2017, 9, 1, 0, 0, 0, 0))
        self.assertEqual(days[10], datetime(2017, 9, 11, 0, 0, 0, 0))
        self.assertEqual(days[29], datetime(2017, 9, 30, 0, 0, 0, 0))

    def test_iterate_date_range(self):
        """Hint: don't return a list."""
        days = []
        start = datetime(2017, 9, 1, 0, 0, 0, 0)
        stop = datetime(2017, 9, 3, 11, 0, 0, 0)
        for d in date_range(start, stop, timedelta(hours=2)):
            days.append(d)

        self.assertEqual(days[0], start)
        self.assertEqual(days[3], datetime(2017, 9, 1, 6, 0, 0, 0))
        self.assertEqual(days[-1], datetime(2017, 9, 3, 10, 0, 0, 0))


class ConvertingStringsIntoDatetimes(TestCase):

    def test_parse_datetime(self):
        text = '2017-09-20 13:09:23'

        self.fail('Write a single line expression')

        self.assertEqual(d.year, 2017)
        self.assertEqual(d.month, 9)
        self.assertEqual(d.day, 20)
        self.assertEqual(d.hour, 13)
        self.assertEqual(d.minute, 9)
        self.assertEqual(d.second, 23)

    def test_format_datetime(self):
        d = datetime(2017, 9, 20, 13, 9, 23)

        self.fail('Write a single line expression')

        self.assertEqual(text, 'Wednesday September 20, 2017 13:09:23')


class ManipulatingDatesUsingTimeZones(TestCase):

    def test_convert_datetime_to_bangalore_time(self):
        """Hint: use 3rd party package to localise the date first.
        Once converted, you can convert it to Bangalore time.
        The timezone for Bangalore is Asia/Kolkata. The local
        date should be Europe/London.
        """
        d = datetime(2017, 9, 10, 9, 30, 0)

        self.fail('Do datetime conversion')

        self.assertEqual(c.year, 2017)
        self.assertEqual(c.month, 9)
        self.assertEqual(c.day, 10)
        self.assertEqual(c.hour, 14)
        self.assertEqual(c.minute, 0)
        self.assertEqual(c.second, 0)
