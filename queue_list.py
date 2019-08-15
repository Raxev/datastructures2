class Queue():
    """
    This Queue class is the Python list implementation of a Queue.
    
    The instances variables of this class include:
    1. self._items: the Python list that holds the data for the Queue.
    
    The class methods include: 
    a. __init__: This method creates the Python list instance variable.
    b. is_empty: This method returns True, if the queue is empty or 
                 False otherwise.
    c. __len__: This method returns the number of items in the Queue.
    d. enqueue: This method adds the passed in item to the Queue in 
                the back.
    e. dequeue: This method removes and returns the first item in 
                the Queue.
    """
    def __init__(self):
        """
        This method creates the empty Queue which is represented 
        by a Python list instance variable.
        """
        self._items = list()

    def is_empty(self):
        """
        This method returns True, if the Queue is empty or False 
        otherwise.
        """
        return len(self) == 0

    def __len__(self):
        """
        This method returns the number of items in the Queue.
        """
        return len(self._items)

    def enqueue(self, item):
        """
        This method adds the passed in item to the Queue in the back.
        :type item: object
        """
        self._items.append(item)

    def dequeue(self):
        """
        This method removes and returns the first item in the Queue.
        """
        return self._items.pop(0)
