# -*- coding: utf-8 -*-

"""Chapter 5: Files and I/O."""
import os
from io import StringIO
from unittest import TestCase

from pythoncookbook.code.chapter5 import (create_temp_file,
                                          iter_records,
                                          read_into_buffer)


class ReadingAndWritingTextDataTest(TestCase):

    def test_open_file_preserving_line_endings(self):
        self.fail('Read hello.txt but preserve the windows line ending.')

        self.assertEqual(contents, 'hello\r\n')

    def test_open_ignore_non_ascii_characters(self):
        self.fail('Read sample.txt and ignore the non-ascii character.')

        self.assertEqual(contents, 'Jalapeo')


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

    def tearDown(self):
        try:
            os.remove('data/somefile')
        except OSError:
            pass


class PerformingIOOperationsOnAStringTest(TestCase):

    def test_write_binary_string_to_file_like_object(self):
        self.fail('Write a single line expression')
        s.write(b'some binary data')

        self.assertEqual(s.getvalue(), b'some binary data')


class ReadingAndWritingCompressedDataFilesTest(TestCase):

    def test_read_compressed_file(self):
        """Read the data/compressed.txt.gz file"""
        self.fail('Write a single line expression')
        text = f.read()
        f.close()

        self.assertEqual(text, 'hello world\n')

    def test_read_compressed_file_alternative(self):
        with open('data/compressed.txt.gz', 'rb') as f: # Note the 'b'

            self.fail('Read the compressed binary file')

            self.assertEqual(text, 'hello world\n')


class IteratingOverFixedSizeRecordsTest(TestCase):

    def test_iterate_over_fixed_size_records(self):
        """Hint: use functools.partial() together with the other version
        of iter() for this one. Open the file in binary mode.
        """
        records = iter_records('data/records.txt', record_size=10)

        records = list(records)

        self.assertEqual(records[0], b'Strings ar')
        self.assertEqual(records[3], b'opular typ')


class ReadingBinaryDataIntoAMutableBufferTest(TestCase):

    def test_read_file_into_buffer(self):
        """Hint: the buffer must be initialised to the
        correct size.
        """
        with open('data/sample.bin', 'wb') as f:
            f.write(b'Hello World')

        buf = read_into_buffer('data/sample.bin')

        self.assertEqual(buf, bytearray(b'Hello World'))
        os.remove('data/sample.bin')

    def test_manipulate_string_in_memory(self):
        buf = bytearray(b'Hello World')

        self.fail('Wrap and manipulate the string')

        # Note: asserting the exact same variable. Don't reassign it.
        self.assertEqual(buf, bytearray(b'Hello WORLD'))


class ManipulatingPathnamesTest(TestCase):

    def test_split_file_extension(self):
        path = '/some/file/path.txt'

        self.fail('Write a single line expression')

        self.assertEqual(split, ('/some/file/path', '.txt'))


class TestingForExistenceOfAFileTest(TestCase):

    def test_get_file_size(self):
        file = 'data/file1.bin'

        self.fail('Write a single line expression')

        self.assertEqual(size, 11)

    def test_get_modified_time(self):
        file = 'data/file1.bin'
        os.utime(file, (1506886291.0, 1506886291.0))

        self.fail('Write a single line expression')

        self.assertEqual(mtime, 1506886291.0)


class AddingOrChangingTheEncodingOfAnAlreadyOpenFileTest(TestCase):

    def test_change_encoding(self):
        file = 'data/file1.bin'

        try:
            f = open(file, encoding='utf-8')
            self.fail('Change the encoding of "f" to latin-1')

            self.assertEqual(f.encoding, 'latin-1')
        finally:
            f.close()


class WritingBytesToATextFileTest(TestCase):

    def test_write_bytes(self):
        try:
            with open('text.txt', 'wt') as text:
                self.fail('Write a byte string to the text file')

            with open('text.txt') as inp:
                self.assertEqual(inp.read(), 'Hello World')
        finally:
            try:
                os.remove('text.txt')
            except OSError:
                pass


class WrappingAnExistingFileDescriptorAsAFileObjectTest(TestCase):

    def test_write_to_file_descriptor(self):
        """Hint: don't try and write directly. Need to wrap."""
        try:
            fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

            self.fail('Write text to the file')

            with open('somefile.txt') as inp:
                self.assertEqual(inp.read(), 'Hello World')
        finally:
            try:
                os.remove('somefile.txt')
            except OSError:
                pass


class MakingTemporaryFilesAndDirectoriesTest(TestCase):

    def test_make_temporary_file(self):
        with create_temp_file() as f:
            f.write('Hello World')
            f.seek(0)
            data = f.read()

            self.assertEqual(data, 'Hello World')

    def test_make_temporary_file_alternate(self):
        self.fail('Make a temporary file')

        f.write('Hello World')
        f.seek(0)
        data = f.read()

        self.assertEqual(data, 'Hello World')
        f.close()  # deletes the file

    def test_make_named_temporary_file(self):
        self.fail('Make a named temporary file')

        self.assertTrue(hasattr(f, 'name'))
        f.close()  # deletes the file

    def test_make_named_temporary_file_prefix_suffix(self):
        self.fail('Make a named temporary file')

        self.assertTrue(os.path.basename(f.name).startswith('foo'))
        self.assertTrue(os.path.basename(f.name).endswith('bar'))
        f.close()  # deletes the file


class SerializingPythonObjectsTest(TestCase):

    def test_pickle_unpickle_object_to_from_file(self):
        to_pickle = list('helloworld')

        self.fail('Pickle then unpickle the object to/from a file')

        self.assertEqual(unpickled, list('helloworld'))

    def test_pickle_unpickle_object_to_from_string(self):
        to_pickle = [1, 2, 3, 4, 5]

        self.fail('Pickle then unpickle the object to/from a bytes object')

        self.assertEqual(unpickled, [1, 2, 3, 4, 5])

    def test_unpickle_multiple_objects_same_file(self):
        """Pay attention to the fact that a single file can contain
        pickled objects of different types, and that the pickle mechanism
        takes care of maintaining type information.
        """
        self.fail('Unpickle the objects from pickled.bin')

        self.assertEqual(obj1, 'helloworld')
        self.assertEqual(obj2, [1, 2, 3, 4, 5])
        self.assertEqual(obj3, {'Apple', 'Pear', 'Banana'})

