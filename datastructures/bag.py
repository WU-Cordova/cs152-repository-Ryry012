from typing import Iterable, Optional, Dict, Iterator
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self._items: Dict[T, int] = {}
        if items and items[0] is not None:
            for item in items[0]:
                self.add(item)

    def add(self, item: T) -> None:
        if item is None:
            raise TypeError("Cannot add None to bag")
        self._items[item] = self._items.get(item, 0) + 1

    def remove(self, item: T) -> None:
        if item is None:
            raise TypeError("Cannot remove None from bag")
        if item not in self._items:
            raise ValueError(f"Item {item} not in bag")
        self._items[item] -= 1
        if self._items[item] == 0:
            del self._items[item]

    def count(self, item: T) -> int:
        if item is None:
            raise TypeError("Cannot count None in bag")
        return self._items.get(item, 0)

    def __len__(self) -> int:
        return sum(self._items.values())

    def distinct_items(self) -> Iterable[T]:
        return self._items.keys()

    def __contains__(self, item) -> bool:
        if item is None:
            raise TypeError("Cannot check for None in bag")
        return item in self._items

    def clear(self) -> None:
        self._items.clear()