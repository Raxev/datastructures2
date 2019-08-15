from abc import ABC, abstractmethod
class Comparable():
    """
    This class uses a class variable to count the number of times 
    the compare method is called.  It is designed to be inherited  
    from classes that implement the compare method, who want to 
    keep a count of the number of compares performed in the program.
    The subclass should first call this base class compare method, 
    and then do the comparison between itself and another object 
    of its same type.
    
    This class can also be used to force the subclass who inherits 
    from it to implement the compare method without needing to 
    count the compares. 
    
    The class variable is __num_compares and it is initialized to 0.
    
    The abstract method is compare and the other two class methods
    are:
    1. get_num_compares(cls): returns the number of compares     
    2. clear_compares(cls): resets the number of compares to 0.    
    """ 
    
    __num_compares = 0 

    @abstractmethod     
    def compare(object):
        Comparable.__num_compares += 1
    
    @classmethod
    def get_num_compares(cls):
        return Comparable.__num_compares
    
    @classmethod
    def clear_compares(cls):
        Comparable.__num_compares = 0
