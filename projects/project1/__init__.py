from typing import Iterable, Optional
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__dict_count = {}

    def add(self, item: T) -> None:
        if item is None:
            raise TypeError("Can't be None")
        if item in self.__dict_count:
            self.__dict_count[item] += 1
        else:
            self.__dict_count[item] = 1

    def remove(self, item: T) -> None:
        if item not in self.__dict_count:
            raise ValueError("Not in bag")
        else:
            if self.__dict_count[item] > 1:
                self.__dict_count[item] -= 1
            else:
                del self.__dict_count[item]

    def count(self, item: T) -> int:
        return self.__dict_count.get(item, 0)

    def __len__(self) -> int:
        return sum(self.__dict_count.values())

    def distinct_items(self) -> int:
        return self.__dict_count.keys()

    def __contains__(self, item) -> bool:
        return item in self.__dict_count

    def clear(self) -> None:
        self.__dict_count.clear()
w