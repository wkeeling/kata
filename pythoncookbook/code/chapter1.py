from typing import Generator, Sequence, TextIO


class World:
    def __init__(self, name: str):
        self.name = name


def search(
    f: TextIO, search_string: str, history: int = 10
) -> Generator[tuple[str, Sequence[str]], None, None]:
    yield "", [""]


class Item:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Item({self.name:!r})"


class PriorityQueue:

    def __init__(self):
        pass

    def push(self, item: Item, priority: int) -> None:
        pass

    def pop(self) -> Item:
        pass


def dedupe(seq, key=None):
    pass


def group_by_date(rows):
    pass
