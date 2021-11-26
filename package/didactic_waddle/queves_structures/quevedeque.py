from collections import deque
from typing import NoReturn, Any
from .queveexceptions import FullException, EmptyException


class QueveDeque:
    def __init__(self, size: int = 0) -> NoReturn:
        self._queve = deque()
        self._size = size

    def isEmpty(self) -> bool:

        return not bool(self._queve)

    def getFrontElement(self) -> Any:

        try:
            return self._queve[0]
        except IndexError:
            raise EmptyException

    def getRearElement(self) -> Any:

        try:
            return self._queve[len(self._queve)-1]
        except IndexError:
            raise EmptyException

    def put(self, value: Any) -> NoReturn:

        if len(self._queve) < self._size:
            self._queve.append(value)
        else:
            raise FullException

    def remove(self) -> Any:

        try:
            return self._queve.pop()
        except IndexError:
            raise EmptyException
