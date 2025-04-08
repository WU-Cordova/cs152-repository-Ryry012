from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        self._maxsize = maxsize
        self._data_type = data_type
        self._circularqueue = Array(maxsize, data_type)
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueue(self, item: T) -> None:
        if self.full:
            raise IndexError('Queue is full')
        self._circularqueue[self._rear] = item
        self._rear = (self._rear + 1) % self._maxsize
        self._size += 1

    def dequeue(self) -> T:
        if self.empty:
            raise IndexError('Queue is empty')
        item = self._circularqueue[self._front]
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
            raise IndexError('Queue is empty')
        return self._circularqueue[self._front]

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
        if not isinstance(other, CircularQueue):
            return False
        if self._size != other._size:
            return False
        for i in range(self._size):
            if self._circularqueue[(self._front + i) % self._maxsize] != other._circularqueue[(other._front + i) % other._maxsize]:
                return False
        return True   
    
    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        items = []
        for i in range(self._size):
            items.append(str(self._circularqueue[(self._front + i) % self._maxsize]))
        return f"[{', '.join(items)}]"

    def __repr__(self) -> str:
        return f'CircularQueue(maxsize={self._maxsize}, data_type={self._data_type})'