"""Simple class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__("5_base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Initialize the rectangle 
    """
    def __init__(self, width, height):

        super().__init__()
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
        