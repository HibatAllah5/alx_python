"""Simple module with a Rectangle class that inherits BaseGeometry.
"""

class Rectangle():
    """Simple class Rectangle with width, height and input validation.
    """

    def __init__(self, width, height):
        """Initialize the rectangle after checking if the values passed are
        valid integers using it's superclass method.
        """
        super().__init__()
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the Area of a Rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """Generates a human readable string that represents the Rectangle
        """
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
    