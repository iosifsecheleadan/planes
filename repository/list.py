from error.error import RepositoryError

class List:
    def __init__(self) -> None:
        self.__list = []

    def getList(self):
        return self.__list