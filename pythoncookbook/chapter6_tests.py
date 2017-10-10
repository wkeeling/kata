"""Chapter 6: Data Encoding and Processing."""

from collections import namedtuple
from io import StringIO
from unittest import TestCase

from pythoncookbook.code.chapter6 import dict_to_xml


class ReadingAndWritingCSVDataTest(TestCase):

    def test_read_csv(self):
        with open('data/stocks.csv') as f:
            self.fail('Read the CSV file into a list of rows')

        self.assertEqual(len(rows), 7)
        self.assertEqual(rows[0][1], 'Symbol')
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
        self.assertEqual(rows[4]['Change'], -0.25)
        self.assertEqual(rows[4]['Volume'], 225400)

    def test_write_csv(self):
        headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
        rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
                ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
                ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
                ]

        f = StringIO()

        self.fail('Write the csv data into the StringIO object')

        self.assertEqual(f.getvalue(), """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000""")

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

        self.assertEqual(f.getvalue(), """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000""")

    def test_read_csv_converting_values(self):
        """Hint: apply the conversion to each row as it is read in."""
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
