"""Chapter 4: Iterators and Generators."""

from collections import defaultdict
from unittest import TestCase

from pythoncookbook.chapter4 import (Countdown,
                                     flatten,
                                     frange,
                                     LineHistory,
                                     Node,
                                     skip_initial_lines)


class ManuallyConsumingAnIteratorTest(TestCase):

    def test_iterate_file_without_using_for_loop(self):
        """Hint: load the contents of data/file1.txt"""
        self.fail('Write code to iterate file without using for loop')

        self.assertListEqual(lines, ['hello', 'world', 'foo', 'bar', 'baz'])

    def test_iterate_file_without_using_for_loop_without_using_stopiteration(self):
        """Hint: don't catch StopIteration on this one."""
        self.fail('Write code to iterate file without using for loop')

        self.assertListEqual(lines, ['hello', 'world', 'foo', 'bar', 'baz'])


class CreatingNewIterationPatternsWithGeneratorsTest(TestCase):

    def test_create_generator_that_returns_floating_point_numbers(self):
        floats = list(frange(0, 4, 0.5))

        self.assertListEqual(floats, [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5])


class ImplementingTheIteratorProtocolTest(TestCase):

    def test_iterate_nodes_depth_first(self):
        """Hint: this uses a custom object that implements the iterator
        protocol (already implemented). However, it requires implementation
        of the depth_first() method to support the alternative way of
        iterating the child nodes.
        """
        root = Node(0)
        child1 = Node(1)
        child2 = Node(2)
        root.add_child(child1)
        root.add_child(child2)
        child3 = Node(3)
        child4 = Node(4)
        child1.add_child(child3)
        child1.add_child(child4)
        child5 = Node(5)
        child2.add_child(child5)

        nodes = list(root.depth_first())

        self.assertListEqual(nodes, [root, child1, child3, child4, child2,
                                     child5])


class IteratingInReverseTest(TestCase):

    def test_reverse_file_contents(self):
        self.fail('Reverse the contents of file2.txt')

        self.assertListEqual(file2, [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_reverse_user_defined_class(self):
        c = Countdown(9)

        r = list(reversed(c))

        self.assertListEqual(r, [1, 2, 3, 4, 5, 6, 7, 8, 9])


class DefiningGeneratorsWithExtraStateTest(TestCase):

    def test_access_line_history(self):
        """Hint: similar to the find_lines_wth_history test in ch. 1
        but different in how it iterates the lines and accesses the history.
        """
        found = {}
        with open('data/find_lines_with_history.txt') as f:
            lines = LineHistory(f)
            for line in lines:
                if 'python' in line:
                    found[line] = list(lines.history)

        self.assertEqual(len(found), 2)
        self.assertEqual(found['line8 python'],
                         [(5, 'line5'), (6, 'line6'), (7, 'line7')])
        self.assertEqual(found['line14 python'],
                         [(11, 'line11'), (12, 'line12'), (13, 'line13')])


class TakingASliceOfAnIteratorTest(TestCase):

    def test_slice_generator(self):
        def count():
            for i in range(100):
                yield i

        self.fail('Write a single line expression')

        self.assertListEqual(sliced, [5, 6, 7, 8, 9, 10])


class SkippingTheFirstPartOfAnIterableTest(TestCase):

    def test_skip_initial_lines_with_comments(self):
        """Hint: assume you don't know how many initial comments there are
        and the number of them might vary.
        """
        lines = skip_initial_lines('data/initial_comments.txt')

        self.assertListEqual(lines, [
            'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false',
            'root:*:0:0:System Administrator:/var/root:/bin/sh',
            '# Some other comment'
        ])


class IteratingOverAllPossibleCombinationsOrPermutationsTest(TestCase):

    def test_rearrange_into_permutations(self):
        """Hint: shuffle the items of the list into all possible
        combinations.
        """
        items = ['a', 'b', 'c']

        self.fail('Create permutations of the list of items')

        self.assertListEqual(p, [
            ('a', 'b', 'c'),
            ('a', 'c', 'b'),
            ('b', 'a', 'c'),
            ('b', 'c', 'a'),
            ('c', 'a', 'b'),
            ('c', 'b', 'a')
        ])

    def test_rearrange_into_permutations_smaller_length(self):
        items = ['a', 'b', 'c']

        self.fail('Create permutations of the list of items')

        self.assertListEqual(p, [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'a'),
            ('b', 'c'),
            ('c', 'a'),
            ('c', 'b')
        ])

    def test_produce_combinations(self):
        """Hint: with combinations, the order is not considered. That means
        that (a, b) is the same as (b, a) which is not produced.
        """
        items = ['a', 'b', 'c']

        self.fail('Produce combinations of items')

        self.assertListEqual(c, [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'c')
        ])

    def test_produce_combinations_using_duplicate_items(self):
        items = ['a', 'b', 'c']

        self.fail('Produce combinations of items')

        self.assertListEqual(c, [
            ('a', 'a'),
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'b'),
            ('b', 'c'),
            ('c', 'c')
        ])


class IteratingOverTheIndexPairsOfASequenceTest(TestCase):

    def test_find_lines_words_occurred_on(self):
        word_summary = defaultdict(list)

        with open('words_on_lines.txt', 'r') as f:
            lines = f.readlines()

        self.fail('Populate the word_summary. The key should be the word, '
                  'and the value should be a list of the line numbers '
                  'that contain that word')

        self.assertListEqual(word_summary['is'], [1, 4, 5, 6])

    def test_iterate_sequence_of_tuples(self):
        data = [(1, 2), (3, 4), (5, 6), (7, 8)]
        output = {}

        self.fail('Iterate the sequence of data and add to the output'
                  'dictionary. The key should be the index of the '
                  'tuple in the list, and the value the tuple itself.')

        self.assertEqual(output, {
            0: (1, 2),
            1: (3, 4),
            2: (5, 6),
            3: (7, 8)
        })


class IteratingOverMultipleSequencesSimultaneouslyTest(TestCase):

    def test_iterate_over_two_sequences(self):
        xpts = [1, 5, 4, 2, 10, 7]
        ypts = [101, 78, 37, 15, 62, 99]

        self.fail('Write a single line expression')

        self.assertListEqual(result, [(1, 100), (5, 78), (4, 37), (2, 15),
                                      (10, 62), (7, 99)])

    def test_iterate_two_sequences_different_lengths(self):
        a = [1, 2, 3]
        b = ['w', 'x', 'y', 'z']

        self.fail('Write a single line expression')

        self.assertListEqual(result, [(1, 'w'), (2, 'x'), (3, 'y'),
                                      (None, 'z')])

    def test_iterate_two_sequences_different_lengths_fill_blanks(self):
        a = [1, 2, 3]
        b = ['w', 'x', 'y', 'z']

        self.fail('Write a single line expression')

        self.assertListEqual(result, [(1, 'w'), (2, 'x'), (3, 'y'),
                                      (0, 'z')])

    def test_create_zip_from_two_sequences(self):
        headers = ['name', 'shares', 'price']
        values = ['ACME', 100, 490.1]

        self.fail('Write a single line expression')

        self.assertEqual(result, {
            'name': 'ACME',
            'shares': 100,
            'price': 490.1
        })

    def test_create_output_from_two_sequences(self):
        headers = ['name', 'shares', 'price']
        values = ['ACME', 100, 490.1]

        self.fail('Build the output to satisfy the assertion')

        self.assertEqual(output, 'name=ACME, shares=100, price=490.1')


class IteratingOnItemsInSeparateContainersTest(TestCase):

    def test_iterate_over_iterables(self):
        a = [1, 2, 3, 4, 5]
        b = {6, 7, 8, 9, 10}

        self.fail('Iterate over the iterables in a single loop')

        self.assertListEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_iterate_over_iterables_combine(self):
        """Hint: do this differently from above by combining the lists.
        Note how combining wasn't possible in the last test due to the
        differing types.
        """
        a = [1, 2, 3, 4, 5]
        b = [6, 7, 8, 9, 10]

        self.fail('Iterate over the iterables in a single loop')

        self.assertListEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class CreatingDataProcessingPipelinesTest(TestCase):

    def test_create_pipeline(self):
        """Hint: create the generator functions/expressions below and stack
        them together to form a processing pipeline.
        One of the generators "yields from" one of the others.
        """
        gen_find = None
        gen_opener = None
        gen_concatenate = None
        gen_grep = None

        self.fail('Write the generator expressions and stack them.')

        found = gen_grep('Chelsea', lines)

        self.assertEqual(found, [
            'pythoncookbook/data/file1.tsv:A Brazil  3       4       Defender        27      36      Chelsea         David Luiz      0',
            'pythoncookbook/data/file1.tsv:A Brazil  3       11      Midfielder      22      31      Chelsea         Oscar   0',
            'pythoncookbook/data/file1.tsv:A Brazil  3       16      Midfielder      27      42      Chelsea         Ramires 0',
            'pythoncookbook/data/file1.tsv:A Brazil  3       19      Midfielder      25      7       Chelsea         Willian 0',
            "pythoncookbook/data/file2.tsv:A Cameroon        56      9       Forward 33      117     Chelsea         Samuel Eto'o    c               0"
        ])


class FlatteningANestSequenceTest(TestCase):

    def test_flatten_nested_list(self):
        """Hint: achieve this by using only a single loop within
        flatten().
        """
        items = [1, 2, [3, 4, [5, 6], 7], 8]

        # Produces 1 2 3 4 5 6 7 8
        self.assertEqual(list(flatten(items)), [1, 2, 3, 4, 5, 6, 7, 8])


class IteratingInSortedOrderOverMergedSortedIterablesTest(TestCase):

    def test_iterate_over_merged_sorted_sequences(self):
        """Hint: do not sort the lists again."""
        a = [1, 4, 7, 10]
        b = [2, 5, 6, 11]

        self.fail('Use a single for loop to iterate over the lists together.')

        self.assertEqual(c, [1, 2, 4, 5, 6, 7, 10, 11])


class ReplacingInfiniteWhileLoopsWithAnIteratorTest(TestCase):

    def test_read_file_5_chars_at_a_time(self):
        """Hint: don't use a while loop for this one. Use the
        second form of iter().
        """
        self.fail("Write loop that reads file1.txt 5 chars at a time.")

        self.assertEqual(result, 'hello\nworld\nfoo\nbar\nbaz')

