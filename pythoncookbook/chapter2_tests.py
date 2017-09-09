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

    def 