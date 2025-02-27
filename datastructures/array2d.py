from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):
    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns

        def __getitem__(self, column_index: int) -> T:
            index = self.map_index(self.row_index, column_index)
            return self.array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value 
        
        def map_index(self, row_index: int, column_index: int) -> int:
            return row_index * self.num_columns + column_index

        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(self.num_columns - 1, -1, -1):
                yield self[column_index]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns)])}]'

    def __init__(self, starting_sequence: Sequence[Sequence[T]] = [[]], data_type=object) -> None:
        self.rows = len(starting_sequence)
        self.columns = len(starting_sequence[0]) if self.rows > 0 else 0
        self._data = []

        for row in starting_sequence:
            if len(row) != self.columns:
                raise ValueError("All rows must have the same number of columns.")
            self._data.append(row)

    @staticmethod
    def empty(rows: int = 0, cols: int = 0, data_type: type = object) -> Array2D:
        return Array2D([[data_type() for _ in range(cols)] for _ in range(rows)], data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]:
        if row_index >= self.rows or row_index < -self.rows:
            raise IndexError(f'{row_index} is out of bounds.')
        return Array2D.Row(row_index, self, self.columns)

    def __iter__(self) -> Iterator[Sequence[T]]:
        for row in self._data:
            yield row

    def __reversed__(self):
        for row in reversed(self._data):
            yield row

    def __len__(self):
        return self.rows

    def __str__(self) -> str:
        return f'[{", ".join([str(row) for row in self])}]'

    def __repr__(self) -> str:
        return f'Array2D {self.rows} Rows x {self.columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
