"""Simple module with a Square class that inherits Rectangle.
"""
Rectangle = __import__('7-rectangle').Rectangle


"""Simple class Square with a size as width and height,
    also it has input validation.
"""


"""Initialize the square after checking if the value of size passed is
a valid integer using it's superclass method.

    Arguments:
        size   {int}   --  a positive non zero integer.

    Raises:
        TypeError:  if the size value is not an integer.
        ValueError: if the size value is an integer less or equal to zero.
"""
class Square(Rectangle):
    
    """ Compute the area of a square
        with the formula:
                area = @size ^ 2 = @size * @size
        Return:
                Power of the Square size to 2 or
                size multiplicated by size."""
    
    def __init__(self, size):
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size


    def area(self):
        return self.__size ** 2
    