from error.error import ValidationError

class ValidatorCoordinate:
    def validate(self, coordinate):
        try:
            coordinate.setX(int(coordinate.getX()))
            coordinate.setY(int(coordinate.getY()))
        except ValueError: raise ValidationError('Coordinates must be integers.')


