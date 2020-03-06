from error.error import RepositoryError

from model.board import Board

class Boards:
    def __init__(self) -> None:
        self.__boards = {'playerPlanes' : None,
                         'playerHits' : None,
                         'computerPlanes' : None}

    def getPlayerPlanes(self):
        return self.__boards['playerPlanes']

    def getPlayerHits(self):
        return self.__boards['playerHits']

    def getComputerPlanes(self):
        return self.__boards['computerPlanes']

    def setBoards(self, size):
        board = Board()
        board.getBoardOfSize(size)
        self.__boards['playerPlanes'] = board
        self.__boards['playerHits'] = board
        self.__boards['computerPlanes'] = board


