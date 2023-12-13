"""Simple module with a Rectangle class that inherits BaseGeometry.
"""

class Rectangle():
    """Simple class Rectangle with width, height and input validation.
    """

    def __init__(self, width, height):
        """Initialize the rectangle 
        """
        super().__init__()
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    
        """Computes the Area of a Rectangle.
        """
    def area(self):
        return self.__height * self.__width

    
    """Generates a human readable string that represents the Rectangle
    """
    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
    