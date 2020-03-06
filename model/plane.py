class Plane:
    def __init__(self, head, dir) -> None:
        self.__head = head #coordinate
        self.__direction = dir #string 'up'/'down'/'left'/'right'

    def getHead(self):
        return self.__head

    def getDirection(self):
        return self.__direction

