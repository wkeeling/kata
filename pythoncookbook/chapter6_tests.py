"""Chapter 6: Data Encoding and Processing."""

from collections import namedtuple
from io import StringIO
import os
from unittest import TestCase

from pythoncookbook.code.chapter6 import dict_to_xml


class ReadingAndWritingCSVDataTest(TestCase):

    def test_read_csv(self):
        with open('data/stocks.csv') as f:
            self.fail('Read the CSV file into a list of rows')

        self.assertEqual(len(rows), 7)
        self.assertEqual(rows[0][1], 'Price')
        self.assertEqual(rows[3][3], '9:36am')

    def test_read_csv_named_attributes(self):
        """Hint: each row here is a named tuple."""
        with open('data/stocks.csv') as f:
            self.fail('Read the CSV file into a list of rows')

        self.assertEqual(len(rows), 6)
        self.assertEqual(rows[0].Date, '6/11/2007')
        self.assertEqual(rows[4].Symbol, 'C')

    def test_read_csv_as_sequence_of_dicts(self):
        with open('data/stocks.csv') as f:
            self.fail('Read the CSV file into a list of dicts')

        self.assertEqual(len(rows), 6)
        self.assertEqual(rows[4]['Change'], '-0.25')
        self.assertEqual(rows[4]['Volume'], '360900')

    def test_write_csv(self):
        """Hint: match the line endings."""
        headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
        rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
                ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
                ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
                ]

        f = StringIO()

        self.fail('Write the csv data into the StringIO object')

        self.assertEqual(f.getvalue(), 'Symbol,Price,Date,Time,Change,Volume\n'
                                       'AA,39.48,6/11/2007,9:36am,-0.18,181800\n'
                                       'AIG,71.38,6/11/2007,9:36am,-0.15,195500\n'
                                       'AXP,62.58,6/11/2007,9:36am,-0.46,935000\n')

    def test_write_csv_dict(self):
        headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
        rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
                 'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
                {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
                 'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
                {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
                 'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
                ]

        f = StringIO()

        self.fail('Write the csv data into the StringIO object')

        self.assertEqual(f.getvalue(), 'Symbol,Price,Date,Time,Change,Volume\n'
                                       'AA,39.48,6/11/2007,9:36am,-0.18,181800\n'
                                       'AIG,71.38,6/11/2007,9:36am,-0.15,195500\n'
                                       'AXP,62.58,6/11/2007,9:36am,-0.46,935000\n')

    def test_read_csv_converting_values(self):
        """Hint: create a list of column types and comvert each field."""
        with open('data/stocks.csv') as f:
            self.fail('Read the CSV file into a list of rows, '
                      'converting values')

        self.assertEqual(len(rows), 6)
        self.assertIsInstance(rows[1][0], str)
        self.assertIsInstance(rows[1][1], float)
        self.assertIsInstance(rows[3][5], int)


class ParsingSimpleXMLDataTest(TestCase):

    def test_extract_data_from_xml_file(self):
        with open('data/rss20.xml') as f:
            item = namedtuple('Item', 'title pubDate link')
            self.fail('Parse the file and extract the data')

        self.assertEqual(items[0].title, 'RMOTR: The 3 Python Books you need '
                                         'to get started. For Free.')
        self.assertEqual(items[2].pubDate, 'Sat, 07 Oct 2017 15:51:47 +0000')
        self.assertEqual(items[5].link, 'http://stackabuse.com/scikit-learn-'
                                        'save-and-restore-models/')


class TurningADictionaryIntoXMLTest(TestCase):

    def test_convert_to_xml(self):
        s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
        e = dict_to_xml('stock', s)

        self.fail('Implement dict_to_xml() and then turn resulting root node '
                  'e into a string for the assertion')

        self.assertEqual(result, b'<stock><price>490.1</price><shares>100'
                                 b'</shares><name>GOOG</name></stock>')


class ParsingModifyingAndRewritingXMLTest(TestCase):

    def test_get_root_element(self):
        self.fail('Parse the file data/pred.xml and get the root element')

        self.assertEqual(root.name, 'stop')

    def test_remove_elements(self):
        self.fail('Remove the elements <sri> and <cr> from data/pred.xml '
                  'and write the new XML document to data/pred1.xml')

        with open('data/pred1.xml') as xml:
            content = xml.read()

        self.assertNotIn('<sri>', content)
        self.assertNotIn('<cr>', content)
        os.remove('data/pred1.xml')

    def test_insert_element(self):
        self.fail('Read data/pred.xml and insert a new element after the '
                  '<nm> tag called <spam>test</spam> and write the new XML '
                  'document to data/pred1.xml')

        with open('data/pred1.xml') as f1:
            content = f1.read()

        with open('data/pred_expected.xml') as f2:
            expected = f2.read()

        self.assertEqual(f1, f2)

    def test_get_nth_child(self):
        """Hint: do his without using find or iterating the root node."""
        self.fail('Read data/pred.xml and extract the 1, 2 and 3rd elements')

        self.assertEqual(child_names, ['nm', 'sri', 'cr'])


class InteractingWithARelationalDatabaseTest(TestCase):
    """The tests in this class a interdependent. They won't work
    if executed individually.
    """

    def test_create_database_table(self):
        """Hint: create a table called portfolio with columns symbol (text),
        shares (integer), price (real). Use sqlite3 and use a database file
        of data/test.db. Manually check that the table was created.
        """
        self.fail('Create the database table')

    def test_insert_data(self):
        """Hint: use the same database as created in the previous test,
        and insert the records into it. Manually check that the records
        were inserted.
        """
        stocks = [
            ('GOOG', 100, 490.1),
            ('AAPL', 50, 545.75),
            ('FB', 150, 7.45),
            ('HPQ', 75, 33.2),
        ]
        self.fail('Insert the specified records')

    def test_read_data(self):
        """Hint: use the same database as the previous test and read
        back the records that were previously inserted.
        """
        self.fail('Read all the records in the table')

        self.assertEqual(records, [
            ('GOOG', 100, 490.1),
            ('AAPL', 50, 545.75),
            ('FB', 150, 7.45),
            ('HPQ', 75, 33.2),
        ])

    def test_read_data_parameterized(self):
        """Hint: use the same database as the previous test and read
        back records that have a minimum price of 100."""
        self.fail('Read records with a price over 100')

        self.assertEqual(records, [
            ('GOOG', 100, 490.1),
            ('AAPL', 50, 545.75),
        ])

    @classmethod
    def tearDownClass(cls):
        os.remove('data/test.db')


class DecodingAndEncodingHexadecimalDigitsTest(TestCase):

    def test_encode_as_hex(self):
        s = b'hello'

        self.fail('Write a single line expression')

        self.assertEqual(encoded, b'68656c6c6f')

    def test_encode_as_hex_alternate(self):
        s = b'hello'

        self.fail('Write a single line expression')

        self.assertEqual(encoded, b'68656C6C6F')

    def test_decode_hex(self):
        h = b'68656c6c6f'

        self.fail('Write a single line expression')

        self.assertEqual(decoded, b'hello')

    def test_decode_hex_alternate(self):
        h = b'68656C6C6F'

        self.fail('Write a single line expression')

        self.assertEqual(decoded, b'hello')


class DecodingAndEncodingBase64Test(TestCase):

    def test_encode_as_base64(self):
        s = b'hello'

        self.fail('Write a single line expression')

        self.assertEqual(encoded, b'aGVsbG8=')

    def test_decode_base64(self):
        b = b'aGVsbG8='

        self.fail('Write a single line expression')

        self.assertEqual(decoded, b'hello')
