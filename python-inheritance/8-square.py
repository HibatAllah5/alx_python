"""Defines a Rectangle subclass Square."""


"""Represent a square."""
class Square():

    """Initialize a new square.
    """

    def __init__(self, size):
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __area__(self):
        return self.__size ** 2
