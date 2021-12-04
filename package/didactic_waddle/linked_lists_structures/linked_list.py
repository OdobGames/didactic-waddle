from typing import Any


class LinkedList:

    class __Node:
        def __init__(self, data: Any) -> None:
            self.data = data
            self.next = None

    def __init__(self, *args) -> None:
        self._head = self.__Node
        self._len = 0
        for arg in args:
            self.append(arg)

    def append(self, value) -> None:
        try:
            self._head = self._head(value)
        except TypeError:
            reference = self._head
            while reference.next:
                reference = reference.next
            reference.next = self.__Node(value)
        self._len += 1

    def __iter__(self):
        self._iteration_node = self._head
        return self

    def __next__(self):
        if self._iteration_node is None:
            raise StopIteration
        try:
            return_value = self._iteration_node.data
            self._iteration_node = self._iteration_node.next
            return return_value
        except AttributeError:
            raise StopIteration

    def __len__(self) -> int:
        return self._len

    def __getitem__(self, key: int) -> Any:
        try:
            if abs(key) > self._len:
                raise KeyError('LinkedList index our of range')
        except TypeError:
            raise TypeError(
                f'LinkedList indices must be integers not {type(key).__name__}'
                )
        if key < 0:
            key = self._len + key
        return_value = self._head
        for _ in range(key):
            return_value = return_value.next
        return return_value.data

    def __delitem__(self, key):
        try:
            if abs(key) > self._len:
                raise KeyError('LinkedList index our of range')
        except TypeError:
            raise TypeError(
                f'LinkedList indices must be integers not {type(key).__name__}'
                )
        if key < 0:
            key = self._len + key
        deletion_value = self._head
        deletion_parent = None
        for _ in range(key):
            deletion_parent = deletion_value
            deletion_value = deletion_value.next
        deletion_parent.next = deletion_value.next
        self._len -= 1

    def index(self, value):
        for i, iteration_value in enumerate(self):
            if value == iteration_value:
                return i
        raise ValueError(f'{value} is not in LinkedList')

    def isempty(self):
        return bool(self._len)

    def __str__(self):
        return ','.join([str(x) for x in self])
