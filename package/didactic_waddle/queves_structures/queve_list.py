from typing import Any, NoReturn
from queve_exceptions import EmptyException, FullException

""""Colas implementadas con listas de python"""


class QueveList():

    '''
    Constructor:
    Size= Tamaño de la cola.
    Queve= Se crea una lista vacia.
    '''

    def __init__(self, size: int) -> NoReturn:
        self._size = size
        self._queve = list()

    '''
    Función isEmpty:
    Compara si la cola es igual una lista vacia,
    si es asi retorna True, Si no retorna False.
    '''

    def isEmpty(self) -> bool:

        if self._queve == []:
            return True
        else:
            return False

    '''
    Función getFrontElement:
    Busca el frente de la cola,
    que es el elemento en la posicion 0 de la lista
    Lo retorna si no hay ningun index error,
    si no alza una excepción personalizada.
    '''

    def getFrontElement(self) -> Any:

        try:
            return self._queve[0]
        except IndexError:
            raise EmptyException

    '''
    Función getRearElement:
    Busca el final de la cola, que es el ultimo elemento de la lista,
    es decir la posicion tamaño de la lista menos 1.
    Lo retorna si no hay ningun index error,
    si no alza una excepción personalizada.
    '''

    def getRearElement(self) -> Any:

        try:
            return self._queve[len(self._queve)-1]
        except IndexError:
            raise EmptyException

    '''
    Función put:
    Recibe un valor de cualquier tipo y lo agrega al final de la cola.
    Primero comprueba si el tamaño es el correcto, si es asi lo agrega,
    de lo contrario alza una excepcion personalizada.
    '''

    def put(self, value: Any) -> NoReturn:

        if self._size > len(self._queve):
            self._queve.append(value)
        else:
            raise FullException

    '''
    Función remove:
    Remueve el primer elemento al frente de la cola.
    Si no hay elementos alza una excepcion personalizada.
    '''

    def remove(self) -> NoReturn:

        try:
            self._queve.pop(0)
        except IndexError:
            raise EmptyException
