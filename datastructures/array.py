from __future__ import annotations
from collections.abc import Sequence
from typing import Any, Iterator, Optional, MutableSequence, overload
import numpy as np
from numpy.typing import NDArray

from datastructures.iarray import IArray, T

class Array(IArray[T]):  
    def __init__(self, starting_sequence: MutableSequence[T], data_type: Optional[type]=None) -> None:
        if not isinstance(starting_sequence, Sequence): 
            raise ValueError('Sequence must be a valid sequence type.')
        
        if data_type and not all(isinstance(item, data_type) for item in starting_sequence):
            raise TypeError(f'All items in {starting_sequence} must be of the same type: {data_type}')
        
        self._item_count: int = len(starting_sequence)
        self._data_type: type = data_type or (type(starting_sequence[0]) if starting_sequence else object)
        self._items: NDArray[T] = np.empty(self._item_count or 1, dtype=self._data_type)

        for i in range(self._item_count):
            self._items[i] = starting_sequence[i]

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            if index >= self._item_count or index < -self._item_count:
                raise IndexError(f'{index} is out of bounds.')
            return self._items[index]
        elif isinstance(index, slice):
            return Array(self._items[index].tolist(), self._data_type)
        else:
            raise TypeError('Index must be int or slice.')

    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(index, int):
            raise TypeError('Index must be an int.')
        if not isinstance(item, self._data_type):
            raise TypeError(f'Item must be of type {self._data_type.__name__}')
        if index >= self._item_count or index < -self._item_count:
            raise IndexError(f'{index} is out of bounds.')
        self._items[index] = item

    def append(self, data: T) -> None:
        if self._item_count == len(self._items):
            self._resize(max(1, len(self._items) * 2))
        self._items[self._item_count] = data
        self._item_count += 1

    def append_front(self, data: T) -> None:
        if self._item_count == len(self._items):
            self._resize(max(1, len(self._items) * 2))
        for i in range(self._item_count, 0, -1):
            self._items[i] = self._items[i - 1]
        self._items[0] = data
        self._item_count += 1

    def pop(self) -> None:
        if self._item_count == 0:
            raise IndexError("Pop from empty array")
        self._item_count -= 1

    def pop_front(self) -> None:
        if self._item_count == 0:
            raise IndexError("Pop from empty array")
        for i in range(1, self._item_count):
            self._items[i - 1] = self._items[i]
        self._item_count -= 1

    def __len__(self) -> int:
        return self._item_count

    def _resize(self, new_size: int) -> None:
        new_items: NDArray = np.empty(new_size, dtype=self._data_type)
        for i in range(self._item_count):
            new_items[i] = self._items[i]
        self._items = new_items

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __iter__(self) -> Iterator[T]:
        for i in range(self._item_count):
            yield self._items[i]

    def __reversed__(self) -> Iterator[T]:
        for i in range(self._item_count - 1, -1, -1):
            yield self._items[i]

    def __delitem__(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be int")
        if index >= self._item_count or index < -self._item_count:
            raise IndexError(f'{index} is out of bounds.')
        for i in range(index, self._item_count - 1):
            self._items[i] = self._items[i + 1]
        self._item_count -= 1
        if self._item_count <= len(self._items) // 4:
            self._resize(max(1, len(self._items) // 2))

    def __contains__(self, item: Any) -> bool:
        return any(self[i] == item for i in range(self._item_count))

    def clear(self) -> None:
        self._item_count = 0

    def __str__(self) -> str:
        return str([self._items[i] for i in range(self._item_count)])

    def __repr__(self) -> str:
        return f'Array(logical size: {self._item_count}, physical size: {len(self._items)}, items: {self})'