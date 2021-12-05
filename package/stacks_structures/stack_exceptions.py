class EmptyException(Exception):
    '''Raised when the stack is empty and that generate a error'''

    def __init__(self, message="The stack is empty") -> None:
        self.message = message
        super().__init__(self.message)


class FullException(Exception):
    '''Raised when the stack is full and can't receive new values'''

    def __init__(self, message="The stack can't receive new values") -> None:
        self.message = message
        super().__init__(self.message)
