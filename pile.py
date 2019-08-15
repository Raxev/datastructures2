from card import Card
from stack_llist import Stack

class Pile(Stack):
    """
    This class represents a pile of Cards on the table. This class 
    inherits from the Stack class that is implemented as a LinkedList.
    Since the Pile is a Stack, the Cards are added and removed from 
    the top of the Pile.
    
    The CardSorter holds a Python list of these Pile objects.
    
    There are no instance variables for this class, except for those
    inherited from the Stack or LinkedList classes.
    
    The class methods include 
    a. __init__: This method is the constructor.  It has no instance 
                 variables, except those it inherits from the Stack 
                 class. Call the Stack constructor using super().
    b. add_card: This method pushes the passed in Card onto the top 
                 of the Pile.
    c. get_top_card: This method returns the top Card in the Pile 
                     without removing it
    d. remove_card: This method pops off the top Card from the Pile.
    e. __str__: This method returns a string containing the Cards in 
                this Pile, starting with the first Card as: Rank-Suit 
                Rank-Suit Rank-Suit etc, by calling the string method 
                of the Stack class using super().
    """
    
    def __init__(self):
        """
        This method is the constructor. Call the Stack constructor 
        using super().
        """
        
        ## Add your code here ##
        super().__init__()
    
    def add_card(self, card):
        """
        This method pushes the passed in Card onto the top of 
        the Pile.
        """
        
        ## Add your code here ##
        self.push(card)

    def get_top_card(self):
        """
        This method returns the top Card in the Pile without 
        removing it
        """
        
        ## Add your code here ##
        return self.peek()
        
    def remove_card(self):
        """
        This method pops off the top Card from the Pile
        """
        
        ## Add your code here ##
        return self.pop()

    def __str__(self):
        """
        This method returns a string containing the Cards
        in this Pile, starting with the first Card as:
        Rank-Suit Rank-Suit Rank-Suit etc, by calling the 
        string method of the Stack class using super().
        """
        ## Add your code here ##
        return super().__str__()
