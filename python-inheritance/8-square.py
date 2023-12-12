"""Defines a Rectangle subclass Square."""
Rectangle = __import__('7-rectangle').Rectangle


"""Represent a square."""
class Square(Rectangle):

    """Initialize a new square.

        Args:
            size (int): The size of the new square.
    """
    def __init__(self, size):
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
