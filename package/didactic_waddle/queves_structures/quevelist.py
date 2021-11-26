from typing import Any, NoReturn
from .queveexceptions import FullException, EmptyException


class QuieveList():
    def __init__(self, size: int) -> NoReturn:
        self._size = size
        self._queve = list()

    def isEmpty(self) -> bool:

        if self._queve == []:
            return True
        else:
            return False

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

        if self._size < len(self._queve):
            self._queve.append(value)
        else:
            raise FullException

    def remove(self) -> NoReturn:

        try:
            self._queve.pop(0)
        except IndexError:
            raise EmptyException
