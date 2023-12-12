"""Simple module with the definition of an empty class with an unimplemented
method.
"""

"""Simple empty BaseGeometry class"""
class BaseGeometry():
    """Prototype of the area function that actually isn't implemented. 
    Raises:
        Exception:  a simple exception that tells that the area function is
            not implmenet yet.
    """

    def area(self):
        raise Exception('area() is not implemented')
    