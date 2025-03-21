import os
from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    def __init__(self, max_size: int = 10, data_type=object) -> None:
        self._data = Array[T](max_size, data_type)
        self._top = -1  

    def push(self, item: T) -> None:
        if self.full:
            raise OverflowError("Cannot push: Stack is full")
        self._top += 1
        self._data[self._top] = item

    def pop(self) -> T:
        if self.empty:
            raise IndexError("Cannot pop: Stack is empty")
        item = self._data[self._top]
        self._top -= 1
        return item

    def clear(self) -> None:
        self._top = -1

    def peek(self) -> T:
        if self.empty:
            raise IndexError("Cannot peek: Stack is empty")
        return self._data[self._top]

    @property
    def maxsize(self) -> int:
        return len(self._data)

    @property
    def full(self) -> bool:
        return self._top == self.maxsize - 1

    @property
    def empty(self) -> bool:
        return self._top == -1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IStack) or len(self) != len(other):
            return False
        return all(self._data[i] == other[i] for i in range(len(self)))

    def __len__(self) -> int:
        return self._top + 1

    def __contains__(self, item: T) -> bool:
        return item in self._data[: self._top + 1]

    def __str__(self) -> str:
        return str([self._data[i] for i in range(self._top + 1)])

    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
