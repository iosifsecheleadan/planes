from error.error import ServiceError

class ServiceBoard:
    def __init__(self, repo, valid) -> None:
        self.__repository = repo
        self.__validator = valid

    def setBoards(self,size):
        self.__repository.setBoards(size)

