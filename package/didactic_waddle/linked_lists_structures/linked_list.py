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

    def isempty(self):
        return bool(self._len)
