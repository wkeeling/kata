"""Chapter 7: Functions."""

from unittest import TestCase

from pythoncookbook.code.chapter7 import (add,
                                          recv,
                                          spam)


class WritingFunctionsThatAcceptOnlyKeywordArgumentsTest(TestCase):

    def test_write_function_that_specifies_keyword_only_argument(self):
        self.fail('Write the recv() function where the block argument '
                  'must be passed keyword-only.')
        recv(1024, block=True)


class AttachingInformationalMetadataToFunctionArgumentsTest(TestCase):

    def test_annotate_function(self):
        self.fail('Annotate the add() function')

        self.assertEqual(add.__annotations__, {
            'y': int.__class__, 'return': int.__class__, 'x': int.__class__
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
        funcs[0](2) = 0
        funcs[1](2) = 2
        funcs[2](2) = 4
