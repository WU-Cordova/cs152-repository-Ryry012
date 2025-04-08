import os
from typing import Iterator, TypeVar, Generic, List

T = TypeVar('T')

class Array(Generic[T]):
    def __init__(self, size: int, data_type: type = object) -> None:
        self._data = [None] * size
        self._data_type = data_type

    def __getitem__(self, index: int) -> T:
        return self._data[index]

    def __setitem__(self, index: int, value: T) -> None:
        self._data[index] = value

class IStack(Generic[T]):
    def push(self, item: T) -> None:
        raise NotImplementedError

    def pop(self) -> T:
        raise NotImplementedError

class ArrayStack(IStack[T]):
    def __init__(self, max_size: int = 0, data_type: type = object) -> None:
        self._maxsize = max_size
        self._stack = Array(max_size, data_type)
        self._top = 0
        self._data_type = data_type

    def push(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError(f"Expected {self._data_type}, got {type(item)}")
        if self.full:
            raise IndexError('Stack is full')
        self._stack[self._top] = item
        self._top += 1

    def pop(self) -> T:
        if self.empty:
            raise IndexError('Stack is empty')
        self._top -= 1
        item = self._stack[self._top]
        self._stack[self._top] = None
        return item

    def clear(self) -> None:
        for i in range(self._top):
            self._stack[i] = None
        self._top = 0

    @property
    def peek(self) -> T:
        if self.empty:
            raise IndexError('Stack is empty')
        return self._stack[self._top - 1]

    @property
    def maxsize(self) -> int:
        return self._maxsize

    @property
    def full(self) -> bool:
        return self._maxsize > 0 and self._top == self._maxsize

    @property
    def empty(self) -> bool:
        return self._top == 0

    def __iter__(self) -> Iterator[T]:
        for i in reversed(range(self._top)):
            yield self._stack[i]

    def __len__(self) -> int:
        return self._top

    def __contains__(self, item: T) -> bool:
        return any(x == item for x in self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayStack):
            return False
        return list(self) == list(other)

    def __str__(self) -> str:
        return str(list(self))

    def __repr__(self) -> str:
        return f"ArrayStack(maxsize={self.maxsize}, items={list(self)})"

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is {filename}. Run your tests instead.')