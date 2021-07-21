"""Chapter 2: Strings and Text."""

import fnmatch
import html
import re
from unittest import TestCase


class SplitStringOnMultipleDelimetersTest(TestCase):

    def test_split_string(self):
        """Hint: str.split() won't work for this one.

        Use an alternative split()
        """
        line = 'asdf fjdk; afed, fjek,asdf, foo'

        split = re.split(r'[;,\s]\s*', line)

        self.assertListEqual(split, ['asdf', 'fjdk', 'afed', 'fjek', 'asdf',
                                     'foo'])


class MatchingTextAtStartAndEndOfStringTest(TestCase):

    def test_filter_filenames_with_multiple_extensions(self):
        """Hint: filter the list but don't use more than one conditional
        expression."""
        filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']

        filtered = [f for f in filenames if f.endswith(('.c', '.h'))]

        self.assertListEqual(filtered, ['foo.c', 'spam.c', 'spam.h'])


class MatchingStringsUsingShellWildcardPatternsTest(TestCase):

    def test_match_filename_string(self):
        """Hint: use a wildcard for the match."""
        names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

        matched = [n for n in names if fnmatch.fnmatch(n, '*.csv')]

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

        streets = [s for s in addresses if fnmatch.fnmatch(s, '*ST')]

        self.assertListEqual(streets, ['5412 N CLARK ST', '1060 W ADDISON ST',
                                       '2122 N CLARK ST'])

    def test_match_streets_2(self):
        """Hint: only use one wildcard *"""
        addresses = [
            '5412 N CLARK ST',
            '5423 N CLARK ST',
            '1060 W ADDISON ST',
            '1039 W GRANVILLE AVE',
            '2122 N CLARK ST',
            '4802 N BROADWAY',
        ]

        streets = [s for s in addresses if fnmatch.fnmatch(s, '54*ST')]

        self.assertListEqual(streets, ['5412 N CLARK ST', '5423 N CLARK ST'])


class SearchingAndReplacingTextTest(TestCase):

    def test_replace_substrings(self):
        """Hint: don't use str.replace()."""
        text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

        new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

        self.assertEqual(new_text,
                         'Today is 2012-11-27. PyCon starts 2013-3-13.')


class StripUnwantedCharactersFromStringsTest(TestCase):

    def test_strip_characters_from_ends(self):
        """Hint: don't use more than one function call."""
        t = '-----hello====='

        stripped = t.strip('-=')

        self.assertEqual(stripped, 'hello')


class AligningTextStringsTest(TestCase):

    def test_align_string_left(self):
        """Hint: two ways to do this. Try both.
        Max width is 20 chars."""
        text = 'Hello World'

        aligned = text.ljust(20)
        aligned = format(text, '<20')

        self.assertEqual(aligned, 'Hello World         ')

    def test_align_string_right(self):
        """Hint: two ways to do this. Try both."""
        text = 'Hello World'

        aligned = text.rjust(20)
        aligned = format(text, '>20')

        self.assertEqual(aligned, '         Hello World')

    def test_align_string_center(self):
        """Hint: two ways to do this. Try both."""
        text = 'Hello World'

        aligned = text.center(20)
        aligned = format(text, '^20')

        self.assertEqual(aligned, '    Hello World     ')

    def test_align_non_string(self):
        x = 1.2345

        aligned = format(x, '>10')

        self.assertEqual(aligned, '    1.2345')

    def test_align_non_string_decimal_places(self):
        x = 1.2345

        aligned = format(x, '^10.2f')

        self.assertEqual(aligned, '   1.23   ')


class CombiningAndConcatenatingStringsTest(TestCase):

    def test_build_output_from_generator(self):
        def sample():
            yield 'Is'
            yield 'Chicago'
            yield 'Not'
            yield 'Chicago?'

        built = ' '.join(sample())

        self.assertEqual(built, 'Is Chicago Not Chicago?')


class InterpolatingVariablesInStringsTest(TestCase):

    def test_format_local_vars(self):
        name = 'Guido'
        n = 37

        formatted = '{name} has {n} messages.'.format(**locals())

        self.assertEqual(formatted, 'Guido has 37 messages.')

    def test_format_vars_from_object(self):
        class Info:
            def __init__(self, name, n):
                self.name = name
                self.n = n

        a = Info('Guido', 37)

        formatted = '{name} has {n} messages.'.format_map(vars(a))

        self.assertEqual(formatted, 'Guido has 37 messages.')


class HandlingHtmlAndXmlEntitiesInTextTest(TestCase):

    def test_escape_text(self):
        s = 'Elements are written as "<tag>text</tag>".'

        escaped = html.escape(s)

        self.assertEqual(escaped, 'Elements are written as &quot;&lt;tag&gt;'
                                  'text&lt;/tag&gt;&quot;.')

    def test_escape_text_not_quotes(self):
        s = 'Elements are written as "<tag>text</tag>".'

        escaped = html.escape(s, quote=False)

        self.assertEqual(escaped, 'Elements are written as "&lt;tag&gt;text'
                                  '&lt;/tag&gt;".')

    def test_unescape_text(self):
        """Hint: look to xml.sax"""
        from xml.sax.saxutils import unescape
        t = 'The prompt is &gt;&gt;&gt;'

        unescaped = unescape(t)
        unescaped = html.unescape(t)

        self.assertEqual(unescaped, 'The prompt is >>>')


class PerformingTextOperationsOnByteStringsTest(TestCase):

    def test_slice_byte_string(self):
        data = b'Hello World'

        hello = data[:5]

        self.assertEqual(hello, b'Hello')

    def test_slice_byte_array(self):
        data = bytearray(b'Hello World')

        hello = data[:5]

        self.assertEqual(hello, bytearray(b'Hello'))

    def test_split_byte_array(self):
        data = bytearray(b'Hello World')

        parts = data.split()

        self.assertEqual(parts, [bytearray(b'Hello'), bytearray(b'World')])

    def test_index_byte_string(self):
        """Index the first letter of the string."""
        b = b'Hello World'

        h = b[0]

        self.assertEqual(h, 72)