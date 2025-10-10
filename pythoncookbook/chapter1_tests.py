"""Chapter 1: Data Structures and Algorithms."""

from pathlib import Path

# flake8: noqa
from statistics import mean

import pytest

from pythoncookbook.code.chapter1 import (
    Item,
    PriorityQueue,
    World,
    dedupe,
    group_by_date,
    search,
)


class TestUnpackingSequence:

    def test_unpack_sequence(self):
        record = ("ACME", 50, 91.1, (2012, 12, 21))

        pytest.fail("Unpack record into individual variables")

        assert name == "ACME"
        assert shares == 50
        assert price == 91.1
        assert date == (2012, 12, 21)

    def test_unpack_sequence_nested_tuple(self):
        record = ("ACME", 50, 91.1, (2012, 12, 21))

        pytest.fail("Unpack record into individual variables")

        assert name == "ACME"
        assert shares == 50
        assert price == 91.1
        assert year == 2012
        assert month == 12
        assert day == 21

    def test_unpack_sequence_string(self):
        string = "Hello"

        pytest.fail("Unpack string into individual variables")

        assert a == "H"
        assert b == "e"
        assert c == "l"
        assert d == "l"
        assert e == "o"

    def test_unpack_sequence_object(self):
        w = World("World")

        a, b, c, d, e = w

        assert a == "W"
        assert b == "o"
        assert c == "r"
        assert d == "l"
        assert e == "d"


class TestUnpackingElementsFromIterablesArbitraryLength:

    def test_drop_first_last(self):
        grades = [56, 77, 75, 68, 53, 62, 44]

        pytest.fail("Unpack grades into individual variables")

        assert first == 56
        assert mean(middle) == 67
        assert last == 44

    def test_unpack_phone_numbers(self):
        record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")

        pytest.fail("Unpack record into individual variables")

        assert name == "Dave"
        assert email == "dave@example.com"
        assert phone_numbers == ["773-555-1212", "847-555-1212"]

    def test_unpack_last(self):
        values = [5, 8, 3, 1, 9]

        pytest.fail("Unpack values into individual variables")

        assert mean(first_four) == 4.25
        assert last == 9

    def test_iterate_varying_length_tuples(self):
        records = [
            ("foo", 1, 2),
            ("bar", "hello"),
            ("foo", 3, 4),
        ]

        def do_foo(x, y):
            print("foo", x, y)

        def do_bar(s):
            print("bar", s)

        pytest.fail("Iterate records calling appropriate function")

    def test_unpack_split_string(self):
        line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"

        pytest.fail("Unpack line into individual variables")

        assert uname == "nobody"
        assert homedir == "/var/empty"
        assert sh == "/usr/bin/false"


class TestKeepingTheLastNItems:

    def test_find_lines_with_history(self):
        """Tip: the search function can be implemented as a generator.
        Think about the data structure used to keep track of the history.
        """
        found = {}
        with open(Path(__file__).parent / "data" / "find_lines_with_history.txt") as f:
            for line, prevlines in search(f, "python", history=5):
                found[line] = list(prevlines)
                for pline in prevlines:
                    print(pline)
                print(line)

        assert len(found) == 2
        assert found["line8 python"] == ["line3", "line4", "line5", "line6", "line7"]
        assert found["line14 python"] == [
            "line9",
            "line10",
            "line11",
            "line12",
            "line13",
        ]


class TestFindingTheLargestOrSmallestNItems:

    def test_find_three_largest_items(self):
        """Tip: do this without using slice syntax and do not
        sort the list.
        """
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

        pytest.fail("Find the three largest items in nums")

        assert largest == [42, 37, 23]

    def test_find_three_smallest_items(self):
        """Tip: do this without using slice syntax and do not
        sort the list.
        """
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

        pytest.fail("Find the three smallest items in nums")

        assert smallest == [-4, 1, 2]

    def test_find_three_largest_items_complex(self):
        portfolio = [
            {"name": "IBM", "shares": 100, "price": 91.1},
            {"name": "AAPL", "shares": 50, "price": 543.22},
            {"name": "FB", "shares": 200, "price": 21.09},
            {"name": "HPQ", "shares": 35, "price": 31.75},
            {"name": "YHOO", "shares": 45, "price": 16.35},
            {"name": "ACME", "shares": 75, "price": 115.65},
        ]

        pytest.fail("Find the three most expensive items in portfolio")

        assert (
            expensive
            == [
                {"name": "AAPL", "shares": 50, "price": 543.22},
                {"name": "ACME", "shares": 75, "price": 115.65},
                {"name": "IBM", "shares": 100, "price": 91.1},
            ],
        )


class TestImplementingAPriorityQueue:

    def test_should_get_items_with_highest_priority(self):
        """Tip: PriorityQueue should negate the priority when it
        pushes the item. The items are stored in a tuple in the queue."""

        q = PriorityQueue()
        q.push(Item("foo"), 1)
        q.push(Item("bar"), 5)
        q.push(Item("spam"), 4)
        q.push(Item("grok"), 1)

        assert q.pop().name == "bar"
        assert q.pop().name == "spam"
        assert q.pop().name == "foo"
        assert q.pop().name == "grok"


class TestMappingKeysToMutipleValuesDictionary:

    def test_append_to_list_value(self):
        pytest.fail("Create dictionary 'd' that satisfies the test")

        try:
            d["a"].append(1)
            d["a"].append(2)
            d["b"].append(4)
        except KeyError:
            pass  # Should not raise

        assert d["a"] == [1, 2]


class TestCalculatingWithDictionaries:

    @pytest.fixture
    def prices(self):
        return {
            "ACME": 45.23,
            "AAPL": 612.78,
            "IBM": 205.55,
            "HPQ": 37.20,
            "FB": 10.75,
        }

    def test_find_min_price(self, prices):
        pytest.fail("Find the minimum price of the prices dictionary")

        assert min_price == (10.75, "FB")

    def test_find_max_price(self, prices):
        pytest.fail("Find the maximum price of the prices dictionary")

        assert max_price == (612.78, "AAPL")

    def test_sort_prices(self, prices):
        pytest.fail("Sort prices dictionary by value and return a list of tuples")

        assert (
            prices_sorted
            == [
                (10.75, "FB"),
                (37.2, "HPQ"),
                (45.23, "ACME"),
                (205.55, "IBM"),
                (612.78, "AAPL"),
            ],
        )


class FindingCommonalitiesInTwoDictionariesTest:

    @pytest.fixture
    def dict_a(self):
        return {"x": 1, "y": 2, "z": 3}

    @pytest.fixture
    def dict_b(self):
        return {"w": 10, "x": 11, "y": 2}

    def test_find_keys_in_common(self, dict_a, dict_b):
        pytest.fail("Write a single line expression")

        assert common_keys == {"x", "y"}

    def test_find_keys_in_a_not_b(self, dict_a, dict_b):
        """Hint: think of it as removing b's keys from a."""
        pytest.fail("Write a single line expression")

        assert keys == {"z"}

    def test_find_key_value_pairs_in_common(self, dict_a, dict_b):
        pytest.fail("Write a single line expression")

        assert common_pairs == {("y", 2)}


class RemovingDuplicatesFromASequencePreservingOrderTest:

    def test_dedupe_sequence(self):
        """Hint: dedupe() could also be used to de-dupe any type of iterable,
        not just a list."""
        a = [1, 5, 2, 1, 9, 1, 5, 10]

        b = list(dedupe(a))

        assert b == [1, 5, 2, 9, 10]

    def test_dedupe_sequence_hashable_items(self):
        a = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]

        b = list(dedupe(a, key=lambda d: (d["x"], d["y"])))

        assert b == [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 2, "y": 4}]

        b = list(dedupe(a, key=lambda d: d["x"]))

        assert b == [{"x": 1, "y": 2}, {"x": 2, "y": 4}]


class NamingASliceTest:

    def test_use_named_slice(self):
        record = "....................100          .......513.25     ........"

        pytest.fail("Retrive the information from the string")

        assert shares == 100
        assert price == 513.25


class DeterminingMostFrequentlyOccurringItemsInASequenceTest:

    def test_get_top_three_words(self):
        """Note that counter objects can be combined using mathematical
        operations (little known)."""
        words = [
            "look",
            "into",
            "my",
            "eyes",
            "look",
            "into",
            "my",
            "eyes",
            "the",
            "eyes",
            "the",
            "eyes",
            "the",
            "eyes",
            "not",
            "around",
            "the",
            "eyes",
            "don't",
            "look",
            "around",
            "the",
            "eyes",
            "look",
            "into",
            "my",
            "eyes",
            "you're",
            "under",
        ]

        pytest.fail("Find the top three words")

        assert top_three == [("eyes", 8), ("the", 5), ("look", 4)]


class SortingAListOfDictionariesByAComonKeyTest:

    @pytest.fixture
    def test_rows(self):
        return [
            {"fname": "Brian", "lname": "Jones", "uid": 1003},
            {"fname": "David", "lname": "Beazley", "uid": 1002},
            {"fname": "John", "lname": "Cleese", "uid": 1001},
            {"fname": "Big", "lname": "Jones", "uid": 1004},
        ]

    def test_sort_rows_by_first_name(self, test_rows):
        """Tip: try to avoid using a lambda for the key."""
        pytest.fail("Write a single line expression")

        assert rows_by_fname == [
            {"fname": "Big", "uid": 1004, "lname": "Jones"},
            {"fname": "Brian", "uid": 1003, "lname": "Jones"},
            {"fname": "David", "uid": 1002, "lname": "Beazley"},
            {"fname": "John", "uid": 1001, "lname": "Cleese"},
        ]

    def test_sort_rows_by_first_name_and_last_name(self, test_rows):
        pytest.fail("Write a single line expression")

        assert (
            rows_by_lfname
            == [
                {"fname": "David", "uid": 1002, "lname": "Beazley"},
                {"fname": "John", "uid": 1001, "lname": "Cleese"},
                {"fname": "Big", "uid": 1004, "lname": "Jones"},
                {"fname": "Brian", "uid": 1003, "lname": "Jones"},
            ],
        )


class SortingObjectsWithoutNativeComparisonSupportTest:

    def test_sort_by_user_id(self):
        """Tip: try to avoid using a lambda."""

        class User:
            def __init__(self, user_id):
                self.user_id = user_id

            def __repr__(self):
                return "User({})".format(self.user_id)

        user1 = User(23)
        user2 = User(3)
        user3 = User(99)

        users = [user1, user2, user3]

        pytest.fail("Write a single line expression")

        assert by_user_id == [user2, user1, user3]


class GroupingRecordsBasedOnAFieldTest:

    def test_group_records_by_date(self):
        """Tip: an important step needs to happen before the grouping."""
        rows = [
            {"address": "5412 N CLARK", "date": "07/01/2012"},
            {"address": "5148 N CLARK", "date": "07/04/2012"},
            {"address": "5800 E 58TH", "date": "07/02/2012"},
            {"address": "2122 N CLARK", "date": "07/03/2012"},
            {"address": "5645 N RAVENSWOOD", "date": "07/02/2012"},
            {"address": "1060 W ADDISON", "date": "07/02/2012"},
            {"address": "4801 N BROADWAY", "date": "07/01/2012"},
            {"address": "1039 W GRANVILLE", "date": "07/04/2012"},
        ]

        grouped_by_date = group_by_date(rows)

        assert (
            grouped_by_date["07/01/2012"]
            == [
                {"date": "07/01/2012", "address": "5412 N CLARK"},
                {"date": "07/01/2012", "address": "4801 N BROADWAY"},
            ],
        )

        assert (
            grouped_by_date["07/02/2012"]
            == [
                {"date": "07/02/2012", "address": "5800 E 58TH"},
                {"date": "07/02/2012", "address": "5645 N RAVENSWOOD"},
                {"date": "07/02/2012", "address": "1060 W ADDISON"},
            ],
        )

        assert (
            grouped_by_date["07/03/2012"]
            == [{"date": "07/03/2012", "address": "2122 N CLARK"}],
        )

        assert (
            grouped_by_date["07/04/2012"]
            == [
                {"date": "07/04/2012", "address": "5148 N CLARK"},
                {"date": "07/04/2012", "address": "1039 W GRANVILLE"},
            ],
        )


class FilteringSequenceElementsTest:

    def test_filter_non_numeric_values(self):
        values = ["1", "2", "-3", "-", "4", "N/A", "5"]

        pytest.fail("Write a single line expression")

        assert list(ivals) == ["1", "2", "-3", "4", "5"]

    def test_get_addresses_with_count(self):
        """Tip: this uses something from itertools."""
        addresses = [
            "5412 N CLARK",
            "5148 N CLARK",
            "5800 E 58TH",
            "2122 N CLARK",
            "5645 N RAVENSWOOD",
            "1060 W ADDISON",
            "4801 N BROADWAY",
            "1039 W GRANVILLE",
        ]

        counts = [0, 3, 10, 4, 1, 7, 6, 1]
        more5 = [n > 5 for n in counts]

        pytest.fail("Write a single line expression")

        assert (
            list(greater_than_five)
            == ["5800 E 58TH", "1060 W ADDISON", "4801 N BROADWAY"],
        )


class ExtractingASubsetOfADictionaryTest:

    def test_create_dictionary_of_stocks_over_200(self):
        """Tip: two ways to achieve this using a dict"""
        prices = {
            "ACME": 45.23,
            "AAPL": 612.78,
            "IBM": 205.55,
            "HPQ": 37.20,
            "FB": 10.75,
        }

        pytest.fail("Write a single line expression")

        assert (
            prices_subset
            == {
                "AAPL": 612.78,
                "IBM": 205.55,
            },
        )


class CombineMultipleMappingsInToSingleMappingTest:

    def test_lookup_two_dicts(self):
        a = {"x": 1, "z": 3}
        b = {"y": 2, "z": 4}

        pytest.fail("Write a single line expression")

        assert c["x"] == 1
        assert c["y"] == 2
        assert c["z"] == 3

    def test_mutate_two_dicts(self):
        a = {"x": 1, "z": 3}
        b = {"y": 2, "z": 4}

        pytest.fail("Write a single line expression")

        c["z"] = 10
        c["w"] = 40
        del c["x"]

        assert a == {"w": 40, "z": 10}

        with pytest.raises(KeyError):
            del c["y"]
