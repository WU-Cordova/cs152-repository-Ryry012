from typing import Generic, TypeVar
from datastructures.array import Array
from datastructures.istack import IStack

T = TypeVar('T')

class ArrayStack(IStack[T]):
    def __init__(self, maxsize: int, data_type: type = object) -> None:
        self.maxsize = maxsize
        self._data_type = data_type
        self.stack: Array[T] = Array(maxsize, data_type)
        self.top = -1  # -1 means empty

    def push(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError(f"Expected {self._data_type}, got {type(item)}")
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.stack[self.top] = item

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top + 1 == self.maxsize

    @property
    def empty(self) -> bool:
        return self.is_empty()

    @property
    def full(self) -> bool:
        return self.is_full()

    def __len__(self) -> int:
        return self.top + 1

    def __str__(self) -> str:
        items = [str(self.stack[i]) for i in range(self.top + 1)]
        return f"[{', '.join(items)}]"

    def __repr__(self) -> str:
        return f"ArrayStack(maxsize={self.maxsize}, size={len(self)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayStack):
            return False
        if len(self) != len(other):
            return False
        for i in range(self.top + 1):
            if self.stack[i] != other.stack[i]:
                return False
        return True
