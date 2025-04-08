from collections.abc import Sequence
from abc import ABC, abstractmethod

class Array:
    def __init__(self, sequence):
        if not isinstance(sequence, Sequence):
            raise ValueError("Sequence must be a valid sequence type.")
        self._array = sequence

    def __len__(self):
        return len(self._array)

    def __getitem__(self, index):
        return self._array[index]

    def __setitem__(self, index, value):
        self._array[index] = value

    def __iter__(self):
        return iter(self._array)

class ArrayStack(ABC):
    def __init__(self, capacity):
        self._size = 0
        self._items = Array([None] * capacity)  # Initialize with empty sequence

    def clear(self):
        self._size = 0
        self._items = Array([None] * len(self._items))  # Reset the array to its capacity

    def __contains__(self, item):
        for i in range(self._size):
            if self._items[i] == item:
                return True
        return False

    def push(self, item):
        if self._size < len(self._items):
            self._items[self._size] = item
            self._size += 1
        else:
            raise ValueError("Stack is full.")

    def pop(self):
        if self._size == 0:
            raise ValueError("Stack is empty.")
        item = self._items[self._size - 1]
        self._size -= 1
        return item

    def peek(self):
        if self._size == 0:
            raise ValueError("Stack is empty.")
        return self._items[self._size - 1]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._items)

    def __len__(self):
        return self._size
