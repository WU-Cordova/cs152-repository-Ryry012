import os
from datastructures.istack import IStack, T
from datastructures.linkedlist import LinkedList

class Stack(IStack[T]):
    def __init__(self) -> None:
        self._stack = LinkedList()

    def push(self, item: T) -> None:
        self._stack.append(item)

    def pop(self) -> T:
        return self._stack.pop_back()

    def peek(self) -> T:
        return self._stack.back()

    def size(self) -> int:
        return len(self._stack)

    def is_empty(self) -> bool:
        return self._stack.is_empty()

    def clear(self) -> None:
        self._stack.clear()

    def __contains__(self, item: T) -> bool:
        return self._stack.__contains__(item)

    def __eq__(self, other: object) -> bool:
        return self._stack == other

    def __str__(self) -> str: 
        return str(self._stack)

    def __repr__(self) -> str: 
        return f'Stack({self._stack})'

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
