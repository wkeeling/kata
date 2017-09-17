"""Chapter 4: Iterators and Generators."""

from unittest import TestCase

from pythoncookbook.chapter4 import (Countdown,
                                     frange,
                                     LineHistory,
                                     Node)


class ManuallyConsumingAnIterator(TestCase):

    def test_iterate_file_without_using_for_loop(self):
        """Hint: load the contents of data/file1.txt"""
        self.fail('Write code to iterate file without using for loop')

        self.assertListEqual(lines, ['hello', 'world', 'foo', 'bar', 'baz'])

    def test_iterate_file_without_using_for_loop_without_using_stopiteration(self):
        """Hint: don't catch StopIteration on this one."""
        self.fail('Write code to iterate file without using for loop')

        self.assertListEqual(lines, ['hello', 'world', 'foo', 'bar', 'baz'])


class CreatingNewIterationPatternsWithGenerators(TestCase):

    def test_create_generator_that_returns_floating_point_numbers(self):
        floats = list(frange(0, 4, 0.5))

        self.assertListEqual(floats, [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5,
                                      4.0])


class ImplementingTheIteratorProtocol(TestCase):

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


class IteratingInReverse(TestCase):

    def test_reverse_file_contents(self):
        self.fail('Reverse the contents of file2.txt')

        self.assertListEqual(file2, [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_reverse_user_defined_class(self):
        c = Countdown(9)

        r = list(reversed(c))

        self.assertListEqual(r, [9, 8, 7, 6, 5, 4, 3, 2, 1])


class DefiningGeneratorsWithExtraState(TestCase):

    def test_access_line_history(self):
        """Hint: similar to the find_lines_wth_history test in ch. 1
        but different in how it iterates the lines and accesses the history.
        """
        found = {}
        with open('data/find_lines_with_history.txt') as f:
            lines = LineHistory(f)
            for line in lines:
                if 'python' in line:
                    for lineno, hline in lines.history:
                        print('{}:{}'.format(lineno, hline))

        self.assertEqual(len(found), 2)
        self.assertEqual(found['line8 python'],
                         ['line5', 'line6', 'line7'])
        self.assertEqual(found['line14 python'],
                         ['line11', 'line12', 'line13'])
