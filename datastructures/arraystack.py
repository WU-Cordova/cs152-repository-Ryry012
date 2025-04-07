import os
from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        self._maxsize = max_size
        self.stack = Array(max_size, data_type)
        self._top = 0  # Points to the next empty index

    def push(self, item: T) -> None:
        if self.full:
            raise IndexError('Stack is full')
        self.stack[self._top] = item
        self._top += 1

    def pop(self) -> T:
        if self.empty:
            raise IndexError('Stack is empty')
        self._top -= 1
        item = self.stack[self._top]
        self.stack[self._top] = None  # Optional: Clear reference
        return item

    def clear(self) -> None:
        for i in range(self._top):
            self.stack[i] = None
        self._top = 0

    @property
    def peek(self) -> T:
        if self.empty:
            raise IndexError('Stack is empty')
        return self.stack[self._top - 1]

    @property
    def maxsize(self) -> int:
        return self._maxsize

    @property
    def full(self) -> bool:
        return self._top == self._maxsize

    @property
    def empty(self) -> bool:
        return self._top == 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayStack):
            return False
        if self._top != other._top:
            return False
        for i in range(self._top):
            if self.stack[i] != other.stack[i]:
                return False
        return True

    def __len__(self) -> int:
        return self._top

    def __contains__(self, item: T) -> bool:
        for i in range(self._top):
            if self.stack[i] == item:
                return True
        return False

    def __str__(self) -> str:
        return str([self.stack[i] for i in range(self._top)])

    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
