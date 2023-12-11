class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialises the data"""

        self.size = size

    @property
    def size(self):
        """Getter method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Returns current square area"""
        return (self.__size * self.__size)
    