from error.error import ServiceError

class ServicePlane:
    def __init__(self, repo, valid) -> None:
        self.__repository = repo
        self.__validator = valid

    def validate(self, plane):
        self.__validator.valiadte(plane)

    def verify(self, plane):
        self.__validator.verify(plane, self.__repository)