from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class ArrayStack(IStack[T]):

    def __init__(self) -> None:
        self._data: List[T] = []

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if self.empty:
            raise IndexError("Cannot pop: Stack is empty")
        return self._data.pop()

    def peek(self) -> T:
        if self.empty:
            raise IndexError("Cannot peek: Stack is empty")
        return self._data[-1]

    @property
    def empty(self) -> bool:
        return len(self._data) == 0

    def clear(self) -> None:
        self._data.clear()

    def __contains__(self, item: T) -> bool:
        return item in self._data

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IStack) or len(self) != len(other):
            return False
        return self._data == list(other)

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Stack({self._data})"

    def __repr__(self) -> str:
        return str(self)
