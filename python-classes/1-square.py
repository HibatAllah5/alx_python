"""Defines a square"""
class Square():
    """Define a private attribute size"""
    
    """Initialises the data"""
    def __init__(self, size=0):
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        