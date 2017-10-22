"""Chapter 8: Classes and Objects."""

from unittest import TestCase


class ChangingTheStringRepresentationOfInstancesTest(TestCase):

    def test_define_str_and_repr_methods(self):
        """Hint: think about the way the strings are formatted, in terms
        of special string formatting args that need to be used.
        """
        class Pair:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Pair(3, 4)

        self.fail('Implement the __str__ and __repr__ methods')

        self.assertEqual(str(p), '(3, 4)')
        self.assertEqual(eval(repr(p)), p)


class CustomizingStringFormattingTest(TestCase):

    def test_object_customized_formatting(self):
        """Hint: look carefully at the different ways formatting is
        achieved in the assertions.
        """
        _formats = {
            'ymd': '{d.year}-{d.month}-{d.day}',
            'mdy': '{d.month}/{d.day}/{d.year}',
            'dmy': '{d.day}/{d.month}/{d.year}'
        }

        class Date:
            def __init__(self, year, month, day):
                self.year = year
                self.month = month
                self.day = day

        d = Date(2012, 12, 21)

        self.fail('Implenent the necessary method on the Date class')

        self.assertEqual(format(d), '2012-12-21')
        self.assertEqual(format(d, 'mdy'), '12/21/2012')
        self.assertEqual('The date is {:ymd}'.format(d),
                         'The date is 2012-12-21')


class CreatingManagedAttributesTest(TestCase):

    def test_create_properties(self):
        class Person:
            def __init__(self, first_name):
                pass

        p = Person('John')

        self.fail('Implement the Person class')

        self.assertEqual(a.first_name, 'John')
        with self.assertRaises(TypeError):
            a.first_name = 10
        with self.assertRaises(AttributeError):
            del a.first_name
        with self.assertRaises(TypeError):
            Person(10)


class CallingAMethodOnAParentClassTest(TestCase):

    def test_call_method_in_hierarchy(self):
        class Base:
            pass

        class A(Base):
            pass

        class B(Base):
            def foo(self):
                return 'bar'

        class C(A, B):
            pass

        c = C()

        self.fail('Implement the necessary methods in the hierarchy')

        self.assertEqual(c.foo(), 'bar')

    def test_delegate_call_excluding_special_method(self):
        class Proxy:
            def __init__(self, obj):
                self._obj = obj

        class Foo:
            def hello(self):
                return 'world'

        p = Proxy(Foo())
        setattr(p, 'a', 'b')

        self.fail('Implement he neessary methods on Proxy')

        self.assertEqual(p.hello(), 'world')
        self.assertTrue(hasattr(p, 'a'))

