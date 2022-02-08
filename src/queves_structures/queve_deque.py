from collections import deque
from typing import NoReturn, Any
from queve_exceptions import EmptyException, FullException

"""Colas implementadas con la libreria de una cola doble en python"""


class QueveDeque:

    '''
    Constructor:
    Size= Tamaño de la cola.
    Queve= Se crea una cola doble vacia.
    '''

    def __init__(self, size: int) -> NoReturn:
        self._queve = deque()
        self._size = size

    '''
    Función isEmpty:
    Retorna el booleano de la cola, al estar vacia retornara False,
    o al tener mas de un elemento retorna True.
    Pero al tener not se niega el booleano, consiguiendo asi,
    que si la cola esta vacia sera True si no False.
    '''

    def isEmpty(self) -> bool:

        return not bool(self._queve)

    '''
    Función getFrontElement:
    Busca el elemento al frente de la cola,
    que es el elemento en la posicion 0 de la cola doble
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
    Busca el elemento al final de la cola, que es el ultimo elemento
    a la derecha de la coladoble.
    Es decir la posicion tamaño de la lista menos 1.
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
    Recibe un valor de cualquier tipo y lo agrega al final
    a derecha de la cola doble.
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
    Remueve el primer elemento a la izquierda de la cola doble.
    Si no hay elementos alza una excepcion personalizada.
    '''

    def remove(self) -> Any:

        try:
            return self._queve.popleft()
        except IndexError:
            raise EmptyException
