from typing import Any, Generic, TypeVar
from datastructures.array import Array
from datastructures.iqueue import IQueue

T = TypeVar('T')

class CircularQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = [None] * maxsize
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.maxsize:
            raise IndexError("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.maxsize
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.maxsize
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxsize

    def __len__(self):
        return self.size

    def __str__(self):
        items = []
        for i in range(self.size):
            index = (self.front + i) % self.maxsize
            items.append(self.queue[index])
        return str(items)
