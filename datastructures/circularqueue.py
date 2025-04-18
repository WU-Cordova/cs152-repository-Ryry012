from typing import Any, TypeVar
import numpy as np

from datastructures.array import Array
from datastructures.iqueue import IQueue

T = TypeVar('T')

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        starting_sequence = [data_type() for _ in range(maxsize + 1)]
        self.circularqueue = Array(starting_sequence=starting_sequence, data_type=data_type)
        self._front = 0
        self._rear = 0

    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue '''
        if self.full:
            raise IndexError("Queue is full")
        self.circularqueue[self._rear] = item
        self._rear = (self._rear + 1) % len(self.circularqueue)

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue '''
        if self.empty:
            raise IndexError("Queue is empty")
        item = self.circularqueue[self._front]
        self._front = (self._front + 1) % len(self.circularqueue)
        return item

    def clear(self) -> None:
        ''' Removes all items from the queue '''
        self.circularqueue = Array([None] * len(self.circularqueue))
        self._front = 0
        self._rear = 0

    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it '''
        if self.empty:
            raise IndexError("Queue is empty")
        return self.circularqueue[self._front]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise '''
        return (self._rear + 1) % len(self.circularqueue) == self._front

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise '''
        return self._front == self._rear
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue '''
        return len(self.circularqueue) - 1

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise '''
        if not isinstance(other, CircularQueue):
            return False
        
        if len(self) != len(other):
            return False
        
        for i in range(len(self)):
            self_idx = (self._front + i) % len(self.circularqueue)
            other_idx = (other._front + i) % len(other.circularqueue)
            if self.circularqueue[self_idx] != other.circularqueue[other_idx]:
                return False
        
        return True

    def __len__(self) -> int:
        ''' Returns the number of items in the queue '''
        return (self._rear - self._front + len(self.circularqueue)) % len(self.circularqueue)

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue showing just the values '''
        elements = []
        for i in range(len(self)):
            idx = (self._front + i) % len(self.circularqueue)
            element = self.circularqueue[idx]
            if hasattr(element, 'item'):  # Handle numpy types
                elements.append(str(element.item()))
            else:
                elements.append(str(element))
        return f"CircularQueue([{', '.join(elements)}])"

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object '''
        return f"CircularQueue(maxsize={self.maxsize}, data_type={self.circularqueue.data_type})"