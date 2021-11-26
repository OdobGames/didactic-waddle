from queue import Queue
from typing import Any, NoReturn


class QueveQueve:
    def __init__(self, size: int = 0) -> NoReturn:
        self._queve = Queue(size)

    def isEmpty(self) -> bool:
        return self._queve.empty()

    def getFrontElement(self) -> Any:
        pass

    def getRearElement(self) -> Any:
        pass

    def put(self, n) -> NoReturn:

        self._queve.put(n)

    def remove(self) -> NoReturn:

        self._queve.get()
