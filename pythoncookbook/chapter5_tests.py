# -*- coding: utf-8 -*-

"""Chapter 5: Files and I/O."""

from io import StringIO
from unittest import TestCase


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