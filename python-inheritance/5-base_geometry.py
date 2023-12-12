"""Simple module with the definition of an empty class with an unimplemented
method and a validator function.
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
    
    """Verify if value is a valid integer value.
    Arguments:
        name {str}      --  a string related with the value.
        value {object}  --  the value that will be checked.
    Raises:
            TypeError:  if value is not an integer.
            ValueError: if value is an integer less or equal to zero.
        """    
 
    def integer_validator(self, name, value):
        
        if name is not None and len(name) > 0:
            if type(value) is not int:
                raise TypeError('{:s} must be an integer'.format(name))
            if value <= 0:
                raise ValueError('{:s} must be greater than 0'.format(name))
            