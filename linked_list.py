from twoway_node import Node, TwoWayNode


class LinkLyst(object):
    """
    Creates a linked list object consisting of one way nodes or two way nodes,
    with the link list being prefixed as singly or doubly respectivley.
    The link variable allows for the selection between the two types of nodes
    by passing the string 'single' or 'double'. The linked list may be created
    by passing an iterable collection, along with a boolean value to the reverse
    parameter to indicate if the ordering of the collection should be reversed
    in the linked list. If no collection is passed, then simply instantiate
    the linked list with a link type, and populate the structure with data using 
    the insert method. The methods pop and remove delete data from the linked
    list by indexing or specifying a target item respectivley, with only the
    pop method returning the deleted item. Getting and setting data by indexing
    is also supported. Singly linked lists only support nonnegative indexing
    in order to increase the visibility of the structure's one directional
    nature. Doubly linked lists support both positive and negative indexing,
    indicative of the ability for two way nodes to point bidirectionally. For 
    additional information regarding the two implementations of linked lists 
    please use help(Node) or help(TwoWayNode).
    """
    
    def __init__(self, collection=None, link='single', reverse=False):
        """Creates a linked list object."""
        LinkLyst.check_data(collection, reverse)
        if link == 'single':
            self.create_single(collection, reverse)
        elif link == 'double':
            self.create_double(collection, reverse)
        else:
            raise TypeError("link must either be 'single' or 'double'.")
     
    def check_data(collection, reverse):
        """Check parameters passed in the initialization of the linked list."""
        if collection is not None:
            try:
                _ = iter(collection)
            except TypeError as error:
                raise error
        if (reverse is not True) and (reverse is not False):
            raise TypeError("reverse must either be True or False.")

    def create_single(self, collection, reverse):
        """Creates a singly linked list."""
        self._lyst = Node()
        if collection is not None:
            if reverse is False:
                temp = Node()
                for item in collection:
                    temp.insert(item)
                for item in temp:
                    self.insert(item)
            else:            
                for item in collection:
                    self.insert(item) 
                     
    def create_double(self, collection, reverse):
        """Creates a doubly linked list."""
        self._lyst = TwoWayNode()
        if collection is not None:
            if reverse is False:
                index = -1
            else:
                index = 0
            for item in collection:
                self.insert(item, index)
            
    def get_lyst(self):
        """-> the linked list of nodes."""
        return self._lyst

    def __len__(self):
        """-> size of the linked list."""
        return len(self.get_lyst())  

    def __str__(self):
        """-> string representation of the linked list."""
        return str(self.get_lyst())
    
    def __iter__(self):
        """Allows for iteration through the linked list."""
        return iter(self.get_lyst())      
            
    def insert(self, item, index=None):
        """Insert data method by indexing."""
        self.get_lyst().insert(item, index)
        
    def pop(self, index=None):
        """Delete data by indexing. -> deleted data."""
        return self.get_lyst().pop(index)
    
    def remove(self, target_item):
        """Delete data by specifying a target item."""
        return self.get_lyst().remove(target_item)
    
    def __getitem__(self, index):
        """Get data from the linked list by indexing."""
        return self.get_lyst()[index]
    
    def __setitem__(self, index, new_item):
        """Overwrite existing data in the linked list by indexing."""
        self.get_lyst()[index] = new_item
    
    def __eq__(self, other):
        """Test for equality between a linked list and another object."""
        return self.get_lyst() == other.get_lyst()

        