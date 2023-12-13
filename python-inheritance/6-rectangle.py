"""Simple module with a Rectangle class that inherits BaseGeometry.
"""

"""Simple class Rectangle with width, height and input validation.
"""
class Rectangle():

    
    """Initialize the rectangle after checking if the values passed are
    valid integers using it's superclass method.
    """
    def __init__(self, width, height):

        super().__init__()
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
        