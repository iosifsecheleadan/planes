from validator.coordinate import ValidatorCoordinate
from validator.plane import ValidatorPlane
from validator.board import ValidatorBoard

from repository.list import List
from repository.board import Boards

from service.plane import ServicePlane
from service.board import ServiceBoard

from ui.console import Console


validCoord = ValidatorCoordinate()

validPlane = ValidatorPlane()
repoPlane = List()
servPlane = ServicePlane(repoPlane, validPlane)

validBoard = ValidatorBoard()
repoBoard = Boards()
servBoard = ServiceBoard(repoBoard, validBoard)

console = Console(servBoard, servPlane, validCoord)

console.run()
