from datastructures.iqueue import IQueue
from datastructures.linkedlist import LinkedList
from typing import TypeVar, Generic

T = TypeVar('T')

class Deque(IQueue[T]):
    def __init__(self, data_type: type = object) -> None:
        self._list = LinkedList[T](data_type)

    def enqueue(self, item: T) -> None:
        self._list.append(item)

    def dequeue(self) -> T:
        return self._list.pop_front()

    def enqueue_front(self, item: T) -> None:
        self._list.prepend(item)

    def dequeue_back(self) -> T:
        return self._list.pop()

    def front(self) -> T:
        return self._list.front()

    def back(self) -> T:
        return self._list.back()

    def empty(self) -> bool:
        return self._list.empty()

    def __len__(self) -> int:
        return len(self._list)

    def __contains__(self, item: T) -> bool:
        return item in self._list

    def __eq__(self, other) -> bool:
        return isinstance(other, Deque) and self._list == other._list

    def clear(self):
        self._list.clear()

    def __str__(self) -> str:
        return str(self._list)

    def __repr__(self) -> str:
        return f"Deque({repr(self._list)})"
