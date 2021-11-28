from queue import Queue
from typing import Any, NoReturn
from queveexceptions import EmptyException, FullException


class QueveQueve:
    def __init__(self, size: int) -> NoReturn:

        self._size = size
        self._queve = Queue(size)

    def isEmpty(self) -> bool:

        return self._queve.empty()

    def getFrontElement(self) -> Any:

        try:
            temporal = self._queve.get()
            temporal2 = temporal
            for i in range(0, self._size):
                if i == self._size-1:
                    self._queve.put(temporal2)
                    return temporal
                else:
                    self._queve.put(temporal2)
                    temporal2 = self._queve.get()
            return temporal
        except IndexError:
            raise EmptyException

    def getRearElement(self) -> Any:

        try:
            for i in range(0, self._size):
                temporal = self._queve.get()
                self._queve.put(temporal)
            return temporal
        except IndexError:
            raise EmptyException

    def put(self, n) -> NoReturn:

        if self._size > self._queve.qsize():
            self._queve.put(n)
        else:
            raise FullException

    def remove(self) -> NoReturn:
        try:
            self._queve.get()
        except IndexError:
            raise EmptyException
