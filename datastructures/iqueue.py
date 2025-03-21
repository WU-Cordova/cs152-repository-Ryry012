from typing import Any, Sequence
from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue using an array.
    """
    
    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object. '''
        starting_sequence = [data_type() for _ in range(maxsize + 1)]
        self.circularqueue = Array(starting_sequence=starting_sequence, data_type=data_type)
        self._front = 0
        self._rear = 0

    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue. '''
        if self.full:
            raise IndexError("Queue is full")
        self.circularqueue[self._rear] = item
        self._rear = (self._rear + 1) % len(self.circularqueue)

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue. '''
        if self.empty:
            raise IndexError("Queue is empty")
        item = self.circularqueue[self._front]
        self._front = (self._front + 1) % len(self.circularqueue)
        return item

    def clear(self) -> None:
        ''' Removes all items from the queue. '''
        self.circularqueue = Array(len(self.circularqueue))
        self._front = 0
        self._rear = 0

    @property
    def front(self) -> T:
        ''' Returns the item at the front without removing it. '''
        if self.empty:
            raise IndexError("Queue is empty")
        return self.circularqueue[self._front]

    @property
    def full(self) -> bool:
        ''' Checks if the queue is full. '''
        return (self._rear + 1) % len(self.circularqueue) == self._front

    @property
    def empty(self) -> bool:
        ''' Checks if the queue is empty. '''
        return self._front == self._rear

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue. '''
        return len(self.circularqueue) - 1

    def __eq__(self, other: object) -> bool:
        ''' Checks if two CircularQueues are equal. '''
        if not isinstance(other, CircularQueue):
            return False
        if self._front != other._front or self._rear != other._rear:
            return False
        return all(
            self.circularqueue[(self._front + i) % len(self.circularqueue)] ==
            other.circularqueue[(other._front + i) % len(other.circularqueue)]
            for i in range(len(self))
        )

    def __len__(self) -> int:
        ''' Returns the number of items in the queue. '''
        return (self._rear - self._front + len(self.circularqueue)) % len(self.circularqueue)

    def __str__(self) -> str:
        ''' Returns a string representation of the queue. '''
        return str(self.circularqueue)

    def __repr__(self) -> str:
        ''' Returns a detailed string representation of the queue. '''
        return f'CircularQueue({repr(self.circularqueue)})'
