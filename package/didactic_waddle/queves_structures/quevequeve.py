from queue import Queue
from typing import Any, NoReturn
from queveexceptions import EmptyException, FullException

"""Colas implementadas con la libreria de colas simples en python"""


class QueveQueve:

    '''
    Constructor:
    Size= Tamaño de la cola.
    Queve= Se crea una cola simple vacia.
    '''

    def __init__(self, size: int) -> NoReturn:
        self._size = size
        self._queve = Queue(size)

    '''
    Función isEmpty:
    Retorna el booleano de la cola, al estar vacia retornara False,
    o al tener mas de un elemento retorna True.
    Pero al tener not se niega el booleano, consiguiendo asi,
    que si la cola esta vacia sera True si no False.
    '''

    def isEmpty(self) -> bool:

        return self._queve.empty()

    '''
    Función getFrontElement:
    Busca el elemento al frente de la cola,
    al ser una cola simple solo se puede agregar elementos al final,
    y quitar elementos del frente, por lo tanto se necesitan dos
    variables temporales, la primera obtenga y elimine el primer elemento
    de el frente de la cola y lo guarde, y otra variable igualada
    a la anterior para poder iterarla añadiendola y obteniendola
    de la cola hasta que se complete un ciclo, quedando asi
    guardado el elemento del frente en una variable y poder retornarlo.
    Lo retorna si no hay ningun index error,
    si no alza una excepción personalizada.
    '''

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

    '''
    Función getRearElement:
    Busca el final de la cola.
    De la misma forma con una variable temporal,
    se añade y se obtiene completando un ciclo de iteraciones
    iguales a su tamaño, guardado el ultimo elemento de la cola
    en una variable para poder retornarlo.
    Lo retorna si no hay ningun index error,
    si no alza una excepción personalizada.
    '''

    def getRearElement(self) -> Any:

        try:
            for i in range(0, self._size):
                temporal = self._queve.get()
                self._queve.put(temporal)
            return temporal
        except IndexError:
            raise EmptyException

    '''
    Función put:
    Recibe un valor de cualquier tipo y lo agrega al final de la cola.
    Primero comprueba si el tamaño es el correcto, si es asi lo agrega,
    de lo contrario alza una excepcion personalizada.
    '''

    def put(self, Value: Any) -> NoReturn:

        if self._size > self._queve.qsize():
            self._queve.put(Value)
        else:
            raise FullException

    '''
    Función remove:
    Remueve el primer elemento al frente de la cola.
    Si no hay elementos alza una excepcion personalizada.
    '''

    def remove(self) -> NoReturn:
        try:
            self._queve.get()
        except IndexError:
            raise EmptyException
