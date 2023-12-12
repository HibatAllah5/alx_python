class Square:
    """Defines a square"""

    def __init__(self, size):
        """Initialises the data.

        Args:
            size (int): The size of the new square.
        """

        self.__size = size
        
    def dir(cls):
        return [attribute for  attribute in super().dir() if attribute != "init_subclass"] 
