import os
from datastructures.iqueue import IQueue, T
from datastructures.linkedlist import LinkedList

class Queue(IQueue[T]): 
    def __init__(self) -> None:
        self._queue = LinkedList()

    def enqueue(self, item: T) -> None:
        self._queue.prepend(item)

    def dequeue(self) -> T:
        return self._queue.pop_back()

    def front(self) -> T:
        return self._queue.back()

    def back(self) -> T:
        return self._queue.front()

    def size(self) -> int: 
        return len(self._queue)

    def is_empty(self) -> bool: 
        return self._queue.is_empty()

    def clear(self) -> None: 
        self._queue.clear()


    def __contains__(self, item: T) -> bool:
        for i in self._queue:
            if item == i:
                return True
        return False

    def __eq__(self, other: object) -> bool:
        return self._queue == other

    def __str__(self) -> str: 
        return str(self._queue)

    def __repr__(self) -> str: 
        return f'ListQueue({self._queue})'

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
