"""Defines a square"""
class Square():
    
    """Initialises the data"""
    def __init__(self, size=0):
        
        self.size = size

    """Getter method"""
    @property
    def size(self):
    
        return (self.__size)

    """Setter method"""
    @size.setter
    def size(self, value):
        
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    """Returns current square area"""
    def area(self):
        return (self.__size * self.__size)
    