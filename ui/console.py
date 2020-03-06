from error.error import *

from model.plane import Plane
from model.coordinate import Coordinate

class Console:
    def __init__(self, board, plane, coord) -> None:
        self.__servBoard = board #service
        self.__servPlane = plane #service
        self.__validCoord = coord #service

    def run(self):
        self.__setBoard()
        self.__setPlayerPlanes()
        self.__setComputerPlanes()
        while True:
            self.__playerTurn()
            if self.__checkPlayer():
                self.__messageWon()
                message = 'I want my revenge! Wanna rematch?'
                break
            self.__computerTurn()
            if self.__checkComputer():
                self.__messageLost()
                message = 'Wanna get revenge loser?'
                break
        self.__replay(message)

    def __setBoard(self):
        while True:
            size = input('Give the size of the board (square): ')
            try:
                size = int(size)
                break
            except ValueError: print('Size must be a integer.')
        self.__servBoard.setBoards(size)

    def __setPlayerPlanes(self):
        for number in range(0, 3):
            while True:
                try:
                    plane = self.__userInputPlane()
                    self.__servPlane.validate(plane)
                    self.__servPlane.verify(plane)
                    break
                except ValidationError as message: print(message)


    def __userInputPlane(self):
        plane = input('Give the plane head coordinates (2 integers) and direction(up/down/left/right: ')
        plane = plane.split(' ')
        head = Coordinate(plane[0], plane[1])
        plane = Plane(head, plane[2])
        return plane

    def __replay(self, message='Would you like to replay?'):
        while True:
            replay =input(message + ' (Yes/No)')
            if replay is 'Yes':
                break
            elif replay is 'No':
                return
            else: print('When I say Yes/No, I mean Yes/No.')
        self.run()





