from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterator, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.data_type = data_type
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0


    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type = object) -> LinkedList[T]:
        linked_list = LinkedList(data_type)
        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError(f"Expected {data_type}, got {type(item)}")
            linked_list.append(item)
        return linked_list



    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Expected {self.data_type}, got {type(item)}")
        node = LinkedList.Node(data=item)
        if self.empty:
            self.head = self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Expected {self.data_type}, got {type(item)}")
        node = LinkedList.Node(data=item)
        if self.empty:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.count += 1


    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Expected {self.data_type} for item, got {type(item)}")
        if not isinstance(target, self.data_type):
            raise TypeError(f"Expected {self.data_type} for target, got {type(target)}")
        traveler = self.head
        while traveler:
            if traveler.data == target:
                break
            traveler = traveler.next
        if traveler is None:
            raise ValueError(f"Target {target} not found in linked list")

        if traveler is self.head:
            self.prepend(item)
        else:
            new_node = LinkedList.Node(data=item)
            new_node.previous = traveler.previous
            new_node.next = traveler
            traveler.previous.next = new_node
            traveler.previous = new_node
            self.count += 1



    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Expected {self.data_type} for item, got {type(item)}")
        if not isinstance(target, self.data_type):
            raise TypeError(f"Expected {self.data_type} for target, got {type(target)}")
        traveler = self.head
        while traveler:
            if traveler.data == target:
                break
            traveler = traveler.next
        if traveler is None:
            raise ValueError(f"Target {target} not found in linked list")
        new_node = LinkedList.Node(data=item)
        new_node.previous = traveler
        new_node.next = traveler.next
        if traveler.next:
            traveler.next.previous = new_node
        else:
            self.tail = new_node
        traveler.next = new_node
        self.count += 1


    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Expected {self.data_type}, got {type(item)}")
        traveler = self.head
        while traveler:
            if traveler.data == item:
                if traveler.previous:
                    traveler.previous.next = traveler.next
                else:
                    self.head = traveler.next
                if traveler.next:
                    traveler.next.previous = traveler.previous
                else:
                    self.tail = traveler.previous
                self.count -= 1
                return
            traveler = traveler.next
        raise ValueError(f"{item} not found in linked list")


    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Expected {self.data_type}, got {type(item)}")
        traveler = self.head
        while traveler:
            next_node = traveler.next
            if traveler.data == item:
                if traveler.previous:
                    traveler.previous.next = traveler.next
                else:
                    self.head = traveler.next
                if traveler.next:
                    traveler.next.previous = traveler.previous
                else:
                    self.tail = traveler.previous
                self.count -= 1
            traveler = next_node


    def pop(self) -> T:
        if self.empty:
            raise IndexError("Pop from empty linked list")
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.count -= 1
        return data

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("Pop from empty linked list")
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self.count -= 1
        return data

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("Front from empty linked list")
        return self.head.data
    
    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError("Back from empty linked list")
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.count == 0
    
    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head = None 
        self.tail = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        traveler = self.head
        while traveler:
            if traveler.data == item:
                return True
            traveler = traveler.next
        return False

    def __iter__(self) -> Iterator[T]:
        self.travel_node = self.head
        return self
    
    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data

    def __reversed__(self) -> Iterator[T]:
        self.travel_node = self.tail
        while self.travel_node:
            yield self.travel_node.data
            self.travel_node = self.travel_node.previous
       

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if self.count != other.count:
            return False
        current_self = self.head
        current_other = other.head
        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
