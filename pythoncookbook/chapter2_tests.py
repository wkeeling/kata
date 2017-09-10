from unittest import TestCase


class SplitStringOnMultipleDelimetersTest(TestCase):

    def test_split_string(self):
        """Hint: str.split() won't work for this one.

        Use an alternative split()
        """
        line = 'asdf fjdk; afed, fjek,asdf, foo'

        self.fail('Write a single line expression')

        self.assertListEqual(split, ['asdf', 'fjdk', 'afed', 'fjek', 'asdf',
                                     'foo'])


class MatchingTextAtStartAndEndOfStringTest(TestCase):

    def test_filter_filenames_with_multiple_extensions(self):
        """Hint: filter the list but don't use more than one conditional
        expression."""
        filenames = ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

        self.fail('Write a single line expression')

        self.assertListEqual(filtered, ['foo.c', 'spam.c', 'spam.h'])


class MatchingStringsUsingShellWildcardPatterns(TestCase):

    def test_match_filename_string(self):
        """Hint: use a wildcard for the match."""
        names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

        self.fail('Write a single line expression')

        self.assertListEqual(matched, ['Dat1.csv', 'Dat2.csv'])

    def test_match_streets(self):
        """Hint: use wildcard and simple shell expressions."""
        addresses = [
            '5412 N CLARK ST',
            '1060 W ADDISON ST',
            '1039 W GRANVILLE AVE',
            '2122 N CLARK ST',
            '4802 N BROADWAY',
        ]

        self.fail('Write a single line expression')

        self.assertListEqual(streets, ['5412 N CLARK ST', '1060 W ADDISON ST',
                                       '2122 N CLARK ST'])
    def test_match_single_street(self):
        addresses = [
            '5412 N CLARK ST',
            '1060 W ADDISON ST',
            '1039 W GRANVILLE AVE',
            '2122 N CLARK ST',
            '4802 N BROADWAY',
        ]

        self.fail('Write a single line expression')

        self.assertListEqual(street, ['5412 N CLARK ST'])


class SearchingAndReplacingTextTest(TestCase):

    def test_replace_substrings(self):
        """Hint: don't use str.replace()."""
        text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

        self.fail('Write a single line expression')

        self.assertEqual(new_text,
                         'Today is 2012-11-27. PyCon starts 2013-3-13.')


class StripUnwantedCharactersFromStringsTest(TestCase):

    def test_strip_characters_from_ends(self):
        """Hint: don't use more than one function call."""
        t = '-----hello====='

        self.fail('Write a single line expression')

        self.assertEqual(stripped, 'hello')


class AligningTextStringsTest(TestCase):

    def test_align_string_left(self):
        """Hint: two ways to do this. Try both."""
        text = 'Hello World'

        self.fail('Write a single line expression')

        self.assertEqual(aligned, 'Hello World         ')

    def test_align_string_right(self):
        """Hint: two ways to do this. Try both."""
        text = 'Hello World'

        self.fail('Write a single line expression')

        self.assertEqual(aligned, '         Hello World')

    def test_align_string_center(self):
        """Hint: two ways to do this. Try both."""
        text = 'Hello World'

        self.fail('Write a single line expression')

        self.assertEqual(aligned, '    Hello World     ')

    def test_align_non_string(self):
        x = 1.2345

        self.fail('Write a single line expression')

        self.assertEqual(aligned, '    1.2345')

    def test_align_non_string_decimal_places(self):
        x = 1.2345

        self.fail('Write a single line expression')

        self.assertEqual(aligned, '   1.23   ')


class CombiningAndConcatenatingStringsTest(TestCase):

    def test_build_output_from_generator(self):
        def sample():
            yield 'Is'
            yield 'Chicago'
            yield 'Not'
            yield 'Chicago?'
            yield 12345

        self.fail('Write a single line expression')

        self.assertEqual(built, 'Is Chicago Not Chicago? 12345')