from queue import Queue, Empty, Full
from typing import Any, NoReturn


class QueveQueve:
    def __init__(self, size: int = 0) -> NoReturn:
        self._queve = Queue(size)

    def isEmpty(self) -> bool:
        return self._queve.empty()

    def getFrontElement(self) -> Any:
        try:
            temporal = self._queve.get()
            self._queve.put(temporal)
            return temporal
        except Empty:
            pass

    def getRearElement(self) -> Any:
        try:
            temporal = self._queve.get(False)
            self._queve.put(temporal)
            return temporal
        except Full:
            pass

    def put(self, n) -> NoReturn:

        self._queve.put(n)

    def remove(self) -> NoReturn:

        self._queve.get()
