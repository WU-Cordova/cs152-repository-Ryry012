from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    def __init__(self, maxsize: int = 10, data_type=object) -> None:
        self._maxsize = maxsize
        self._data = Array(maxsize, data_type)
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueue(self, item: T) -> None:
        if self.full:
            raise IndexError("Queue is full")
        self._data[self._rear] = item
        self._rear = (self._rear + 1) % self._maxsize
        self._size += 1

    def dequeue(self) -> T:
        if self.empty:
            raise IndexError("Queue is empty")
        item = self._data[self._front]
        self._front = (self._front + 1) % self._maxsize
        self._size -= 1
        return item

    def clear(self) -> None:
        self._front = 0
        self._rear = 0
        self._size = 0

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("Queue is empty")
        return self._data[self._front]

    @property
    def full(self) -> bool:
        return self._size == self._maxsize

    @property
    def empty(self) -> bool:
        return self._size == 0
    
    @property
    def maxsize(self) -> int:
        return self._maxsize

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CircularQueue) or len(self) != len(other):
            return False
        for i in range(len(self)):
            if self._data[(self._front + i) % self._maxsize] != other._data[(other._front + i) % other._maxsize]:
                return False
        return True
    
    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return str([self._data[(self._front + i) % self._maxsize] for i in range(self._size)])

    def __repr__(self) -> str:
        return f'CircularQueue(maxsize={self._maxsize}, items={str(self)})'
