from typing import Any, Generic, TypeVar
from datastructures.array import Array
from datastructures.iqueue import IQueue

T = TypeVar('T')

class CircularQueue(IQueue[T]):
    def __init__(self, maxsize: int) -> None:
        self.maxsize = maxsize
        self.queue: Array[T] = Array(maxsize, object)
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item: T) -> None:
        if self.is_full():
            raise IndexError("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.maxsize
        self.size += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
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