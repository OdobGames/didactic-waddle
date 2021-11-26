from typing import Any, NoReturn


class quievelist():

    queve=[]

    def __init__(self, queve):
        self._queve = queve

    def isEmpty(self)-> bool:

        if self._queve == []:
            return True
        else:
            return False
    
    def getFrontElement(self)-> Any:

        if self.isEmpty(): 
            return None
        else:
            return self._queve[0]

    def getRearElement(self)-> Any:
        if self.isEmpty():
            return None
        else:
            return self._queve[len(self._queve)-1]

    def put(self, n)-> NoReturn:

        self._queve.append(n)

    def remove(self)-> NoReturn:

        self._queve.pop(0)

