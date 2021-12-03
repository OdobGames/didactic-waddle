from collections import deque
from typing import NoReturn, Any
from stack_exceptions import EmptyException, FullException


class StackDeque:
    def __init__(self, size: int) -> NoReturn:
        self._stack = deque()
        self._size = size

    def isEmpty(self) -> bool:
        return not bool(self._stack)

    def peek(self) -> Any:
        try:
            temporal = self._stack.pop()
            self._stack.append(temporal)
            return temporal
        except IndexError:
            raise EmptyException

    def push(self, value: Any) -> NoReturn:
        if len(self._stack) < self._size:
            self._stack.append(value)
        else:
            raise FullException

    def pop(self) -> Any:
        try:
            return self._stack.pop()
        except IndexError:
            raise EmptyException
