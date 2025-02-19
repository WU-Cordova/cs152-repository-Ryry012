# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from ast import Not
from collections.abc import Sequence
import os
from typing import Any, Iterator, Optional, MutableSequence, overload
import numpy as np
from numpy.typing import NDArray

from datastructures.iarray import IArray, T



class Array(IArray[T]):  

    def __init__(self, starting_sequence: MutableSequence[T], data_type: Optional[type]=None) -> None:
        if not isinstance(starting_sequence, Sequence): 
            raise ValueError('Sequence must be a valid sequence type.')
        
        if data_type and not all(isinstance(item, data_type) for item in starting_sequence):
            raise TypeError(f'All items in  {starting_sequence} must be of the same type: {data_type}')
        
        self._item_count: int = len(starting_sequence)
        self._phyical_size : int = 0
        self._data_type: type = type(starting_sequence[0]) if len(starting_sequence) > 0 else object
        self._items: NDArray[T] = np.empty(self._item_count, dtype=self._data_type)

        for i in range(self._item_count):
            self._items[i] = starting_sequence[i]


    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if not isinstance(index,int) and not isinstance(index,slice):
            raise TypeError(f'Not int or slice')
        
        if not isinstance(index,int) and not isinstance(index,slice):
            raise IndexError(f'Not int or slice')
        
        if isinstance(index, int) :
            if index >= self._item_count or index < -self._item_count:
                raise IndexError(f'{index}is out of bouns.')
    
        if isinstance(index, slice):
            return Array((self._items[index]).tolist(), self._data_type)
    
        return self._items[index]
    
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(index, int) :
            raise TypeError('Index must be Int')
        
        if not isinstance(item, self._data_type) and not isinstance(item, type(self._items[0])): 
            raise TypeError(f'Type must be {self._data_type}')
        
        if index > self._item_count or index < -self._item_count:
            raise IndexError(f'{index}is out of bouns.')
        
        
        self._items[index] = item

    def append(self, data: T) -> None:
        if self._item_count == len(self._items): #out of space
            size = len(self._items) * 2 if len(self._items)> 0 else 1
            self._resize(size)
        
        self[self._item_count] = data
        self._item_count += 1

    def append_front(self, data: T) -> None:
        if self._item_count == len(self._items): #out of space
            size = len(self._items) * 2 if len(self._items)> 0 else 1
            self._resize(size)

        self._item_count += 1

        for index in range(len(self) -1, 0, -1):
            self[index] = self[index-1]

        self[0] = data
        
    
    def pop(self) -> None:
        del self[-1]
    
    def pop_front(self) -> None:
        del self[0]

    def __len__(self) -> int:
        return self._item_count

    def _resize(self, new_size: int) -> None:
        
        defaulf_value = self._data_type()
        new_items:NDArray = np.array([defaulf_value] * new_size, dtype=self._data_type)

        
        for index in range(self._item_count):
            new_items[index] = self[index]

        self._items = new_items


    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Array):
            return False
        if len(self) != len(other):
            return False
        for index in range(len(self)):
            if self[index] != other[index]:
                return False 
        return True

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __iter__(self) -> Iterator[T]:
        for index in range(self._item_count):
            yield self._items[index]

    def __reversed__(self) -> Iterator[T]:
        for index in range(self._item_count - 1, -1 -1):
            yield self._items[index]


    def __delitem__(self, index: int) -> None:
        if isinstance(index, int) :
            if index >= self._item_count or index < -self._item_count:
                raise IndexError(f'{index}is out of bouns.')
            
        for i in range(index, len(self)-1):
            self[i] = self[i+1]
        
        self._item_count -= 1

        if self._item_count <= len(self._items // 4):
            self._resize(self._items // 2)


    def __contains__(self, item: Any) -> bool:
        return any(self[i] == item for i in range(self._item_count))
    
    def __does_not_contain__(self, item: Any) -> bool:
        return not item in self._items

    def clear(self) -> None:
        if self._item_count > 0 :
            for index in range(self._item_count):
                del self[0]
               
        

    def __str__(self) -> str:
        return str(self._items)
    
    def __repr__(self) -> str:
        return f'Array(logical size): {self._item_count}, phyical size: {len(self._items)} item: {str(self._items)}'

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
