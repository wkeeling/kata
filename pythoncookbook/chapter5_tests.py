# -*- coding: utf-8 -*-

"""Chapter 5: Files and I/O."""

from io import StringIO
from unittest import TestCase

from chapter5 import iter_records


class ReadingAndWritingTextDataTest(TestCase):

    def test_open_file_preserving_line_endings(self):
        self.fail('Read hello.txt but preserve the windows line ending.')

        self.assertEqual(contents, 'hello\r\n')

    def test_open_ignore_non_ascii_characters(self):
        self.fail('Read sample.txt and ignore the non-ascii character.')

        self.assertEqual(contents, 'Jalepeo')


class PrintingToAFileTest(TestCase):

    def test_print_to_file(self):
        f = StringIO()

        self.fail('Write a single line expression')

        self.assertEqual(f.getvalue(), 'hello\n')


class PrintingWithADifferentSeparatorOrLineEndingTest(TestCase):

    def test_print_with_comma_as_separator(self):
        """Pay attention to the fact that this technique works
        with sequences of non-strings. str.join() does not."""
        l = ['hello', 'world', 99]
        f = StringIO()

        self.fail('Write a single line expression')

        self.assertEqual(f.getvalue(), 'hello,world,99')

    def test_print_with_different_ending(self):
        """This suppresses the default new line ending."""
        l = range(5)
        f = StringIO()

        self.fail('Write a single line expression')

        self.assertEqual(f.getvalue(), '0 1 2 3 4 ')


class WritingToAFileThatDoesNotAlreadyExistTest(TestCase):

    def test_write_to_file_if_not_exists(self):
        with open('data/somefile', 'wt') as f:
            f.write('Hello\n')

        with self.assertRaises(FileExistsError):
            self.fail('Write to data/somefile')


class PerformingIOOperationsOnAStringTest(TestCase):

    def test_write_binary_string_to_file_like_object(self):
        self.fail('Write a single line expression')
        s.write(b'some binary data')

        self.assertEqual(s.getvalue(), b'some binary data')


class ReadingAndWritingCompressedDataFilesTest(TestCase):

    def test_read_compressed_file(self):
        self.fail('Write a single line expression')
        text = f.read()

        self.assertEqual(text, 'hello world\n')

    def tes_read_compressed_file_alternative(self):
        f = open('data/compressed.txt.gz', 'rb')  # Note the 'b'

        self.fail('Read the compressed binary file')

        self.assertEqual(text, 'hello world\n')


class IteratingOverFixedSizeRecordsTest(TestCase):

    def test_iterate_over_fixed_size_records(self):
        """Hint: use functools.partial() and the other version
        of iter() for this one."""
        records = iter_records('data/records.txt', record_size=10)

        records = list(records)

        self.assertEqual(records[0], 'Strings ar')
        self.assertEqual(records[3], 'opular typ')

