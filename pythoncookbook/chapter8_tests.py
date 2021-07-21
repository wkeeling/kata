"""Chapter 8: Classes and Objects."""

import collections
import math
from unittest import TestCase
import time

from pythoncookbook.code.chapter8 import (Date,
                                          Integer,
                                          IStream,
                                          lazyproperty,
                                          Proxy)


class ChangingTheStringRepresentationOfInstancesTest(TestCase):

    def test_define_str_and_repr_methods(self):
        """Hint: think about the way the strings are formatted, in terms
        of special string formatting args that need to be used.
        """
        class Pair:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __str__(self):
                return f'{(self.x, self.y)}'

            def __repr__(self):
                return f'Pair(x={self.x}, y={self.y})'

        p = Pair(3, 4)

        self.assertEqual(str(p), '(3, 4)')
        self.assertIsInstance(eval(repr(p)), Pair)


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

            def __format__(self, format_spec):
                default = _formats.get('ymd')
                return _formats.get(format_spec, default).format(d=self)

        d = Date(2012, 12, 21)

        self.assertEqual(format(d), '2012-12-21')
        self.assertEqual(format(d, 'mdy'), '12/21/2012')
        self.assertEqual('The date is {:ymd}'.format(d),
                         'The date is 2012-12-21')


class CreatingManagedAttributesTest(TestCase):

    def test_create_properties(self):
        """Hint: attempting to set a non-string
        for first_name should raise a TypeError.
        """
        class Person:
            def __init__(self, first_name):
                self.first_name = first_name

            @property
            def first_name(self):
                return self._first_name

            @first_name.setter
            def first_name(self, first_name):
                if isinstance(first_name, int):
                    raise TypeError()
                self._first_name = first_name

        p = Person('John')

        self.assertEqual(p.first_name, 'John')
        with self.assertRaises(TypeError):
            p.first_name = 10
        with self.assertRaises(AttributeError):
            del p.first_name
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

        self.assertEqual(c.foo(), 'bar')

    def test_delegate_call_excluding_special_method(self):
        class Proxy:
            def __init__(self, obj):
                self._obj = obj

            def __getattr__(self, item):
                return getattr(self._obj, item)

            def __setattr__(self, key, value):
                if key.startswith('_'):
                    super().__setattr__(key, value)
                else:
                    setattr(self._obj, key, value)

        class Foo:
            def hello(self):
                return 'world'

        f = Foo()
        p = Proxy(f)
        setattr(p, 'a', 'b')
        setattr(p, '_a', 'b')

        self.assertEqual(p.hello(), 'world')
        self.assertTrue(hasattr(f, 'a'))
        self.assertTrue(hasattr(p, '_a'))


class CreatingANewKindOfClassOrInstanceAttribute(TestCase):

    def test_create_descriptor(self):
        class Point:
            x = Integer('x')
            y = Integer('y')

            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Point(2, 3)

        self.assertEqual(p.x, 2)
        p.y = 5
        self.assertEqual(p.y, 5)
        with self.assertRaises(TypeError):
            p.x = 2.3  # Can only set integers
        self.assertIsInstance(Point.x, Integer)
        del p.x
        with self.assertRaises(KeyError):
            p.x


class UsingLazilyComputedPropertiesTest(TestCase):

    def test_define_lazy_attribute(self):
        class Circle:
            def __init__(self, radius):
                self.radius = radius

            @lazyproperty
            def area(self):
                print('Computing area')
                return math.pi * self.radius ** 2

        c = Circle(4.0)

        self.assertEqual(c.radius, 4.0)
        self.assertAlmostEqual(c.area(), 50.26548245743669)
        self.assertEqual(c.area.call_count(), 1)
        self.assertAlmostEqual(c.area(), 50.26548245743669)
        self.assertEqual(c.area.call_count(), 1)  # Area is not recalculated


class DefiningAnInterfaceOrAbstractBaseClassTest(TestCase):

    def test_raise_exception_on_instantiate_abc(self):
        with self.assertRaises(TypeError):
            IStream()

    def test_raise_exception_method_missing(self):
        class SocketStream(IStream):
            def read(self):
                pass

        with self.assertRaises(TypeError):
            SocketStream()

    def test_isinstance(self):
        class SocketStream(IStream):
            def read(self):
                pass

            def write(self, data):
                pass

        s = SocketStream()

        self.assertIsInstance(s, IStream)

    def test_register(self):
        class Foobar:
            pass

        IStream.register(Foobar)

        f = Foobar()

        self.assertIsInstance(f, IStream)

    def test_name_five_collection_abcs(self):
        """Name 5 ABCs that define top level types in the collections module.
        """
        abcs = [
            # Add the names
        ]

        self.assertEqual(len(abcs), 5)
        for name in abcs:
            self.assertIn(name, vars(collections))


class DelegatingAttributeAccessTest(TestCase):

    def test_create_proxy(self):
        """Hint: Need to implement get/set/del and handle special methods."""
        class Spam:
            def __init__(self, x):
                self.x = x

            def bar(self, y):
                return 'Spam.bar: {} {}'.format(self.x, y)

        s = Spam(2)
        p = Proxy(s)

        self.assertEqual(p.x, 2)
        self.assertEqual(p.bar(3), 'Spam.bar: 2 3')
        p.x = 37
        self.assertEqual(s.x, 37)
        del p.x
        self.assertFalse(hasattr(s, 'x'))
        p._hello = 'world'
        self.assertTrue(hasattr(p, '_hello'))
        self.assertFalse(hasattr(s, '_hello'))
        del p._hello
        self.assertFalse(hasattr(p, '_hello'))


class DefiningMoreThanOneConstructorInAClassTest(TestCase):

    def test_define_a_second_constructor(self):
        """Think about the reasons why a factory method is a good idea
        over an __init__ that does too much (via *args).

        1. Factory method much clearer and communicates intent.
        2. Better doc. *args __init__ won't show useful help strings
            with argument names.
        3. Simpler __init__ implementation. In fact, __init__ must do as
            little as possible, simply assigning attributes and leaving more
            complex work to specific factory methods.
        """
        a = Date(2012, 12, 21)
        self.assertEqual(a.year, 2012)
        self.assertEqual(a.month, 12)
        self.assertEqual(a.day, 21)

        t = time.localtime()
        b = Date.today()
        self.assertEqual(b.year, t.tm_year)
        self.assertEqual(b.month, t.tm_mon)
        self.assertEqual(b.day, t.tm_mday)