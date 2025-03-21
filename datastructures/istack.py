from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class IStack(ABC, Generic[T]):
    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def peek(self) -> T:
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
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

class ArrayStack(IStack[T]):
    def __init__(self) -> None:
        self._data: List[T] = []

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if self.empty():
            raise IndexError("Cannot pop: Stack is empty")
        return self._data.pop()

    def peek(self) -> T:
        if self.empty():
            raise IndexError("Cannot peek: Stack is empty")
        return self._data[-1]

    def empty(self) -> bool:
        return len(self._data) == 0

    def clear(self) -> None:
        self._data.clear()

    def __contains__(self, item: T) -> bool:
        return item in self._data

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayStack):
            return False
        return self._data == other._data

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Stack({self._data})"

    def __repr__(self) -> str:
        return f"ArrayStack({self._data})"