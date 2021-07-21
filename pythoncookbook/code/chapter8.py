class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError()
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        print(owner, name)


def lazyproperty(func):
    count = 0
    res = None

    def inner(*args, **kwargs):
        nonlocal count
        nonlocal res
        if res is not None:
            return res
        count += 1
        res = func(*args, **kwargs)
        return res

    def call_count():
        return count

    inner.call_count = call_count

    return inner


from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class Proxy:
    pass


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        from datetime import datetime
        now = datetime.now()
        return cls(now.year, now.month, now.day)
