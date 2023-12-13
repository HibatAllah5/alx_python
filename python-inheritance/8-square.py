"""Simple module with a Square class that inherits Rectangle"""

class Square():

    """Initialize a new square.
    """

    def __init__(self, size):
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """Compute the area of a square
    """
    def __area__(self):   
        return self.__size ** 2
