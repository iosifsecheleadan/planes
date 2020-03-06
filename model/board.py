class Board:
    def __init__(self) -> None:
        self.__board = [[]]

    def getBoardOfSize(self, size):
        self.__board = [ [None] * size ] * size
