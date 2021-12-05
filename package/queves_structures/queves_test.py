from time import perf_counter
from random import randint

from queve_deque import QueveDeque
from queve_list import QueveList
from queve_queve import QueveQueve


class QueveTest:
    def __init__(self, own_queve=None) -> None:
        self._queve_versions = [
            QueveDeque,
            QueveList,
            QueveQueve
        ]
        if own_queve is not None:
            self._queve_versions.append((own_queve))

    def initialization(self, size: int, samples: int = 10):
        times = dict()
        for queve_versions in self._queve_versions:
            sum_times = 0
            for _ in range(samples):
                try:
                    toc = perf_counter()
                    _ = queve_versions(size=size)
                    tic = perf_counter()
                    sum_times += (tic - toc)
                except Exception:
                    raise AttributeError
            times[str(queve_versions.__name__)] = sum_times/samples
        return times

    def emptiness(self, size: int, samples: int = 10):
        times = dict()
        for queve_versions in self._queve_versions:
            sum_times = 0
            for _ in range(samples):
                try:
                    tested_queve = queve_versions(size=size)
                    toc = perf_counter()
                    tested_queve.isEmpty()
                    tic = perf_counter()
                    sum_times += (tic - toc)
                except Exception:
                    raise AttributeError
            times[str(queve_versions.__name__)] = sum_times/samples
        return times

    def popping(self, size: int, samples: int = 10):
        times = dict()
        for queve_versions in self._queve_versions:
            sum_times = 0
            for _ in range(samples):
                try:
                    tested_queve = queve_versions(size=size)
                    [tested_queve.put(randint(0, 100)) for _ in range(size)]
                    toc = perf_counter()
                    _ = tested_queve.getFrontElement()
                    tic = perf_counter()
                    sum_times += (tic - toc)
                except Exception:
                    raise AttributeError
            times[str(queve_versions.__name__)] = sum_times/samples
        return times

    def popping_left(self, size: int, samples: int = 10):
        times = dict()
        for queve_versions in self._queve_versions:
            sum_times = 0
            for _ in range(samples):
                try:
                    tested_queve = queve_versions(size=size)
                    [tested_queve.put(randint(0, 100)) for _ in range(size)]
                    toc = perf_counter()
                    _ = tested_queve.getRearElement()
                    tic = perf_counter()
                    sum_times += (tic - toc)
                except Exception:
                    raise AttributeError
            times[str(queve_versions.__name__)] = sum_times/samples
        return times

    def putting(self, size: int, samples: int = 10):
        times = dict()
        for queve_versions in self._queve_versions:
            sum_times = 0
            for _ in range(samples):
                try:
                    tested_queve = queve_versions(size=size)
                    toc = perf_counter()
                    [tested_queve.put(randint(0, 100)) for _ in range(size)]
                    tic = perf_counter()
                    sum_times += (tic - toc)/size
                except Exception:
                    raise AttributeError
            times[str(queve_versions.__name__)] = sum_times/samples
        return times

    def removing(self, size: int, samples: int = 10):
        times = dict()
        for queve_versions in self._queve_versions:
            sum_times = 0
            for _ in range(samples):
                try:
                    tested_queve = queve_versions(size=size)
                    [tested_queve.put(randint(0, 100)) for _ in range(size)]
                    toc = perf_counter()
                    tested_queve.remove()
                    tic = perf_counter()
                    sum_times += (tic - toc)/size
                except Exception:
                    raise AttributeError
            times[str(queve_versions.__name__)] = sum_times/samples
        return times

    def integral_test(self, size: int, samples: int = 10):
        tests = dict()
        tests['__init__'] = self.initialization(size, samples)
        tests['isEmpty'] = self.emptiness(size, samples)
        tests['getFrontElement'] = self.popping(size, samples)
        tests['getRearElement'] = self.popping_left(size, samples)
        tests['put'] = self.putting(size, samples)
        tests['remove'] = self.removing(size, samples)
        return tests
