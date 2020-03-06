from error.error import ValidationError

from validator.coordinate import ValidatorCoordinate

class ValidatorPlane:
    def validate(self, plane):
        self.__validateCoordinate(plane.getHead())
        if plane.getDirection() not in ['up', 'down', 'left', 'right']:
            raise ValidationError('Direction must be "up"/"down"/"left"/"right".')

    def __validateCoordinate(self, coordinate):
        coordValid = ValidatorCoordinate()
        coordValid.validate(coordinate)

    def verify(self, plane, board):
        pass


