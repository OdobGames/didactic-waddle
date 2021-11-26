from typing import Any, NoReturn
from .stackexceptions import FullExcepetion, EmptyException


class StackList:
    def __init__(self, size: int) -> NoReturn:
        self._size = size
        self._stack = list()

    def isEmpty(self) -> bool:
        return not bool(self._stack)

    def peek(self) -> Any:
        try:
            return self._stack[-1]
        except IndexError:
            raise EmptyException

    def push(self, value: Any) -> NoReturn:
        if self._size < len(self.stack):
            self._stack.append(value)
        else:
            raise FullExcepetion

    def pop(self) -> Any:
        try:
            return self._stack.pop()
        except IndexError:
            raise EmptyException
