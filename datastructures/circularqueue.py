from typing import Any, TypeVar

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
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''
        if self.full:
            raise IndexError("Queue is full")
        self.circularqueue[self._rear] = item
        self._rear = (self._rear + 1) % len(self.circularqueue)

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
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
        ''' Returns the item at the front of the queue without removing it

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self.empty:
            raise IndexError("Queue is empty")
        return self.circularqueue[self._front]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 
        
            Returns:
                True if the queue is full, False otherwise
        '''
        return (self._rear + 1) % len(self.circularqueue) == self._front

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        return self._front == self._rear
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue
        
            Returns:
                The maximum size of the queue
        '''
        return len(self.circularqueue) - 1

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - Both objects are CircularQueues
                - They have the same logical sequence of elements (regardless of physical storage)
                - They have the same length
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''
        if not isinstance(other, CircularQueue):
            return False
        
        if len(self) != len(other):
            return False
        
        # Compare the logical sequence of elements
        for i in range(len(self)):
            self_idx = (self._front + i) % len(self.circularqueue)
            other_idx = (other._front + i) % len(other.circularqueue)
            if self.circularqueue[self_idx] != other.circularqueue[other_idx]:
                return False
        
        return True

    def __len__(self) -> int:
        ''' Returns the number of items in the queue
        
            Returns:
                The number of items in the queue
        '''
        return (self._rear - self._front + len(self.circularqueue)) % len(self.circularqueue)

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue
        
            Returns:
                A string representation of the queue
        '''
        elements = []
        for i in range(len(self)):
            idx = (self._front + i) % len(self.circularqueue)
            elements.append(str(self.circularqueue[idx]))
        return f"CircularQueue([{', '.join(elements)}])"

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f"CircularQueue(maxsize={self.maxsize}, data_type={self.circularqueue.data_type})"