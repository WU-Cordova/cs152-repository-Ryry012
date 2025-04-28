import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib
from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]] = None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = Array(
            starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)],
            data_type=LinkedList
        )
        self.count: int = 0
        self.load_factor: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def __getitem__(self, key: KT) -> VT:
        index = self._hash_function(key) % len(self._buckets)
        bucket = self._buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key: KT, value: VT) -> None:
        raise NotImplementedError

    def keys(self) -> Iterator[KT]:
        raise NotImplementedError

    def values(self) -> Iterator[VT]:
        raise NotImplementedError

    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError

    def __delitem__(self, key: KT) -> None:
        raise NotImplementedError

    def __contains__(self, key: KT) -> bool:
        index = self._hash_function(key) % len(self._buckets)
        bucket = self._buckets[index]
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def __len__(self) -> int:
        return self.count

    def __iter__(self) -> Iterator[KT]:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"

    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)
