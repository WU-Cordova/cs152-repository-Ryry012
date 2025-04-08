from typing import Any, Generic, TypeVar
from datastructures.array import Array
from datastructures.iqueue import IQueue

T = TypeVar('T')

class CircularQueue(IQueue[T]):
    def __init__(self, maxsize: int, data_type: type = object) -> None:
        self.maxsize = maxsize
        self._data_type = data_type
        self.queue: Array[T] = Array(maxsize, data_type)
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError(f"Expected {self._data_type}, got {type(item)}")
        if self.is_full():
            raise IndexError("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.maxsize
        self.size += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.maxsize
        self.size -= 1
        return item

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.maxsize

    @property
    def empty(self) -> bool:
        return self.is_empty()

    @property
    def full(self) -> bool:
        return self.is_full()

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        items = []
        for i in range(self.size):
            index = (self.front + i) % self.maxsize
            items.append(str(self.queue[index]))
        return f"[{', '.join(items)}]"

    def __repr__(self) -> str:
        return f"CircularQueue(maxsize={self.maxsize}, size={self.size})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CircularQueue):
            return False
        if len(self) != len(other):
            return False
        for i in range(self.size):
            self_item = self.queue[(self.front + i) % self.maxsize]
            other_item = other.queue[(other.front + i) % other.maxsize]
            if self_item != other_item:
                return False
        return True
