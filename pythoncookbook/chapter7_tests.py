"""Chapter 7: Functions."""

import math
from unittest import TestCase
from urllib.request import urlopen

from pythoncookbook.code.chapter7 import (add,
                                          recv,
                                          sample,
                                          spam)


class WritingFunctionsThatAcceptOnlyKeywordArgumentsTest(TestCase):

    def test_write_function_that_specifies_keyword_only_argument(self):
        """Write the recv() function where the block argument '
        'must be passed keyword-only.
        """
        with self.assertRaises(TypeError):
            recv(1024, True)

        recv(1024, block=True)


class AttachingInformationalMetadataToFunctionArgumentsTest(TestCase):

    def test_annotate_function(self):
        """Annotate the add() function."""
        self.assertEqual(add.__annotations__, {
            'y': int().__class__, 'return': int().__class__, 'x': int().__class__
        })


class DefiningFunctionsWithDefaultArgumentsTest(TestCase):

    def test_default_argument_with_no_value(self):
        """Hint: the second argument should have a default value.
        Pay attention to what the default value should be.
        Remember: defaut values should *never* be mutable objects.
        """
        self.fail('Implement the spam() function')

        self.assertEqual(spam(1), 1)
        self.assertEqual(spam(1, 2), (1, 2))
        self.assertEqual(spam(1, None), (1, None))


class CapturingVariablesInAnonymousFunctionsTest(TestCase):

    def test_remember_iteration_variable(self):
        """Hint: write a list comprehension that creates a lambda
        function for 3 iterations and each function will sum its
        iteration number with the value passed to it.
        """
        self.fail('Create the list comprehension')

        self.assertEqual(len(funcs), 3)
        self.assertEqual(funcs[0](2), 2)
        self.assertEqual(funcs[1](2), 3)
        self.assertEqual(funcs[2](2), 4)


class MakingAnNArgumentCallableWorkTest(TestCase):

    def test_sort_points_according_to_distance_from_other_point(self):
        points = [(1, 2), (3, 4), (5, 6), (7, 8)]

        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return math.hypot(x2 - x1, y2 - y1)

        fixed_point = (4, 3)

        self.fail('Define the function that will sort each point according '
                  'to distance from fixed_point. Note that using distance() '
                  'will not be suitable - because its signature is not '
                  'compatible with key=')

        points.sort(key=None)

        self.assertEqual(sorted_points, [(3, 4), (1, 2), (5, 6), (7, 8)])


class ReplacingSingleMethodClassesWithFunctionsTest(TestCase):

    def test_replace_class_with_function(self):
        """Hint: fairly open-ended this one..."""
        class UrlTemplate:
            def __init__(self, template):
                self.template = template

            def open(self, **kwargs):
                return urlopen(self.template.format_map(kwargs))

        self.fail('Simplify the above by using functions')

        yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}'
                            '&f={fields}')
        for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
            print(line.decode('utf-8'))


class CarryingExtraStateWithCallbackFunctionsTest(TestCase):

    def test_print_sequence_number(self):
        """Hint: there are a number of ways to carry the sequence
        number through into the callback. Write a few.
        """
        def apply_async(func, args, *, callback):
            # Compute the result
            result = func(*args)
            # Invoke the callback with the result
            callback(result)

        # Here is how the code gets used *without* printing a sequence number
        def print_result(result):
            print('Got:', result)

        def add(x, y):
            return x + y

        apply_async(add, (2, 3), callback=print_result)
        apply_async(add, ('hello', 'world'), callback=print_result)

        self.fail('Call apply_async and maintain a sequence number for '
                  'each call, using different techniques to achieve it')


class AccessingVariablesDefinedInsideAClosureTest(TestCase):

    def test_access_closure_variables(self):
        """Hint: you probably wouldn't want to do this in reality,
        when you can just use a callable object to achieve the same thing.
        """
        f = sample()
        self.assertEqual(f(), 'n=0')
        f.set_n(10)
        self.assertEqual(f(), 'n=10')
        self.assertEqual(f.get_n(), 10)


