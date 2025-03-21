from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class IQueue(Generic[T], ABC):
    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def front(self) -> T:
        pass

    @abstractmethod
    def back(self) -> T:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class ArrayQueue(IQueue[T]):
    def __init__(self) -> None:
        self._data: List[T] = []

    def enqueue(self, item: T) -> None:
        self._data.append(item)

    def dequeue(self) -> T:
        if self.empty():
            raise IndexError("Cannot dequeue: Queue is empty")
        return self._data.pop(0)

    def front(self) -> T:
        if self.empty():
            raise IndexError("Cannot get front: Queue is empty")
        return self._data[0]

    def back(self) -> T:
        if self.empty():
            raise IndexError("Cannot get back: Queue is empty")
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)

    def empty(self) -> bool:
        return len(self._data) == 0

    def clear(self) -> None:
        self._data.clear()

    def __contains__(self, item: T) -> bool:
        return item in self._data

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayQueue):
            return False
        return self._data == other._data

    def __str__(self) -> str:
        return f"Queue({self._data})"

    def __repr__(self) -> str:
        return f"ArrayQueue({self._data})"