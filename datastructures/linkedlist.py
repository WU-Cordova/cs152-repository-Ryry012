from typing import TypeVar, Generic, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T, prev: Optional['Node[T]'] = None, next: Optional['Node[T]'] = None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList(ILinkedList[T]):
    def __init__(self, data_type: type = object) -> None:
        self._data_type = data_type
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size = 0
        self._iter_node = None

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type = object) -> 'LinkedList[T]':
        ll = LinkedList(data_type)
        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError("Element type mismatch.")
            ll.append(item)
        return ll

    def append(self, item: T) -> None:
        self._check_type(item)
        new_node = Node(item, self._tail)
        if self._tail:
            self._tail.next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        self._size += 1

    def prepend(self, item: T) -> None:
        self._check_type(item)
        new_node = Node(item, None, self._head)
        if self._head:
            self._head.prev = new_node
        else:
            self._tail = new_node
        self._head = new_node
        self._size += 1

    def insert_before(self, target: T, item: T) -> None:
        self._check_type(item)
        self._check_type(target)
        node = self._find(target)
        if node is None:
            raise ValueError("Target not found.")
        new_node = Node(item, node.prev, node)
        if node.prev:
            node.prev.next = new_node
        else:
            self._head = new_node
        node.prev = new_node
        self._size += 1

    def insert_after(self, target: T, item: T) -> None:
        self._check_type(item)
        self._check_type(target)
        node = self._find(target)
        if node is None:
            raise ValueError("Target not found.")
        new_node = Node(item, node, node.next)
        if node.next:
            node.next.prev = new_node
        else:
            self._tail = new_node
        node.next = new_node
        self._size += 1

    def remove(self, item: T) -> None:
        self._check_type(item)
        node = self._find(item)
        if node is None:
            raise ValueError("Item not found.")
        self._remove_node(node)

    def remove_all(self, item: T) -> None:
        self._check_type(item)
        node = self._head
        while node:
            next_node = node.next
            if node.value == item:
                self._remove_node(node)
            node = next_node

    def pop(self) -> T:
        if self.empty:
            raise IndexError("Pop from empty list.")
        value = self._tail.value
        self._remove_node(self._tail)
        return value

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("Pop from empty list.")
        value = self._head.value
        self._remove_node(self._head)
        return value

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("List is empty.")
        return self._head.value

    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError("List is empty.")
        return self._tail.value

    @property
    def empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return f"({' <-> '.join(str(item) for item in self)})"

    def __repr__(self) -> str:
        return f"LinkedList{str(self)} Count: {self._size}"

    def clear(self) -> None:
        self._head = self._tail = None
        self._size = 0

    def __contains__(self, item: T) -> bool:
        return self._find(item) is not None

    def __iter__(self) -> 'LinkedList[T]':
        self._iter_node = self._head
        return self

    def __next__(self) -> T:
        if self._iter_node is None:
            raise StopIteration
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        return value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        return list(self) == list(other)

    def __reversed__(self) -> 'LinkedList[T]':
        new_list = LinkedList(self._data_type)
        node = self._tail
        while node:
            new_list.append(node.value)
            node = node.prev
        return new_list

    def _find(self, item: T) -> Optional[Node[T]]:
        node = self._head
        while node:
            if node.value == item:
                return node
            node = node.next
        return None

    def _remove_node(self, node: Node[T]) -> None:
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        self._size -= 1

    def _check_type(self, item: T):
        if not isinstance(item, self._data_type):
            raise TypeError(f"Item must be of type {self._data_type.__name__}.")
