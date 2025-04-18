from datastructures.istack import IStack
from datastructures.linkedlist import LinkedList
from typing import TypeVar, Generic

T = TypeVar('T')

class ListStack(IStack[T]):
    def __init__(self, data_type: type) -> None:
        self._list = LinkedList[T](data_type)

    def push(self, item: T):
        self._list.append(item)

    def pop(self) -> T:
        return self._list.pop()

    def peek(self) -> T:
        return self._list.back

    @property
    def empty(self) -> bool:
        return self._list.empty

    def clear(self):
        self._list.clear()

    def __contains__(self, item: T) -> bool:
        return item in self._list

    def __eq__(self, other) -> bool:
        return isinstance(other, ListStack) and self._list == other._list

    def __len__(self) -> int:
        return len(self._list)

    def __str__(self) -> str:
        return str(self._list)

    def __repr__(self) -> str:
        return f"ListStack({repr(self._list)})"
