#Module for Base class
class Base:
#Representation of the Base 
    __nb_objects = 0

    def __init__(self, id=None):
        #Constructor
        if id is not None:
            self.id += 1
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
