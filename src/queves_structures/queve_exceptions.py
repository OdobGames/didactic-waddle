'''
EmptyException: Una excepcion personalizada para cuando la cola esta vacia,
y genera un error.
'''


class EmptyException(Exception):
    '''Raised when the queve is empty and that generate a error'''

    def __init__(self, message="The queve is empty") -> None:
        self.message = message
        super().__init__(self.message)


'''
FullException: Una excepcion personalizada para cuando la cola esta llena,
y no puede recibir nuevos valores.
'''


class FullException(Exception):
    '''Raised when the queve is full and can't receive new values'''

    def __init__(self, message="The queve can't receive new values") -> None:
        self.message = message
        super().__init__(self.message)
