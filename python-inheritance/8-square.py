"""
    Square Module
"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
        Square Class
    """
    def __init__(self, size):
        """
            Initialize the square base on Rectangle
        """
        self.__size = size
        self.integer_validator('size', size)

    def area(self):
        """
        define area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
            __str__
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
    