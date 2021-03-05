from node import Node


class TwoWayNode(Node):
    """
    Creates a two way node object to store data and point to another two way
    node or to a previous one. Default parameters are used to create an empty 
    two way header node. Use TwoWayNode() to instantiate the empty header node 
    before populating with data via the insert method. Inserting data will 
    result in the creation of an iterable structure collectivley refered to as 
    a doubly linked list. Methods are defined to allow for the removal of data 
    by index (pop) or by specifying a target item (remove). Getting and setting 
    data by indexing is also supported.
    """
    
    def __init__(self, data=None, previous=None, next_=None):
        """Creates two way node object."""
        Node.__init__(self, data, next_)
        if previous is None:
            self.previous = self
        else:
            self.previous = previous
            
    def insert(self, item, index=None):
        """Insert data method which creates a linked list of two way nodes. 
        Index must be within range, with default index of 0. """
        if index is None:
            index = 0
        if index >= 0 and index <= len(self):
            probe = self
            while index > 0 and probe.next_ is not self:
                probe = probe.next_
                index -= 1
            probe.next_ = TwoWayNode(item, probe, probe.next_)
            probe.next_.next_.previous = probe.next_
            self.size_inc()
        elif index < 0 and index >= -len(self) - 1:
            index = abs(index) - 1
            probe = self
            while index > 0 and probe.previous is not self:
                probe = probe.previous
                index -= 1
            probe.previous = TwoWayNode(item, probe.previous, probe)
            probe.previous.previous.next_ = probe.previous
            self.size_inc()
        else:
            raise IndexError(\
                  "Index Outside of Bounds: -len(TWNode) - 1 <= index <= len(TWNode).")
            
    def pop(self, index=None):
        """Remove data method from linked list of two way nodes by index. 
        -> removed data. Index must be within range, with default index 
        of 0."""
        if len(self) == 0:
            raise IndexError("len(TWNode) = 0. No item to pop in empty node.")
        if index is None:
            index = 0
        if index >= 0 and index < len(self):
            probe = self 
            while index > 0 and probe.next_.next_ is not self:
                probe = probe.next_
                index -= 1
            removed_data = probe.next_.data
            probe.next_ = probe.next_.next_    
            probe.next_.previous = probe
            self.size_dec()
        elif index < 0 and index >= -len(self):
            index = abs(index) - 1
            probe = self
            while index > 0 and probe.previous.previous is not self:
                probe = probe.previous
                index -= 1
            removed_data = probe.previous.data
            probe.previous = probe.previous.previous
            probe.previous.next_ = probe
            self.size_dec()
        else:
            raise IndexError(\
                  "Index Outside of Bounds: -len(TWNode) <= index < len(TWNode).")
        return removed_data
    
    def __getitem__(self, index):
        """-> data at specified index. Index must be within range."""
        if len(self) == 0:
            raise IndexError("len(TWNode) = 0. Cannot index.")
        if index >= 0 and index < len(self):
            return Node.__getitem__(self, index)
        elif index < 0 and index >= -len(self):
            index = abs(index) - 1
            probe = self
            while index >= 0 and probe.previous is not self:
                probe = probe.previous
                index -= 1
            return probe.data
        else:
            raise IndexError(\
                  "Index Outside of Bounds: -len(TWNode) <= index < len(TWNode).")
    
    def __setitem__(self, index, new_item):
        """Overwrite existing data with a new item at a specified index. Index
        must be within range."""
        if len(self) == 0:
            raise IndexError("len(TWNode) = 0. Cannot index.")
        if index >= 0 and index < len(self):
            Node.__setitem__(self, index, new_item)
        elif index < 0 and index >= -len(self):
            index = abs(index) - 1
            probe = self
            while index >= 0 and probe.previous is not self:
                probe = probe.previous
                index -= 1
            probe.data = new_item
        else:
            raise IndexError(\
                  "Index Outside of Bounds: -len(TWNode) <= index < len(TWNode).")
    
    def __eq__(self, other):
        """Test for equality between a linked list of two way nodes and another 
        object. If the other object is found to be a linked list of two way 
        nodes of the same size, then the equality check will ensure data is not 
        obscured by user perturbation of the size attribute for either operand."""
        len_error = "len(self) = len(other) but strucutres do not match. "\
        "Check <instance>._size for error or broken links."
        if Node.__eq__(self, other) is False:
            return False
        probe_self = self
        probe_other = other
        while probe_self.previous is not self:
            if probe_other.previous is not other:
                probe_self = probe_self.previous
                probe_other = probe_other.previous
                if probe_self.data != probe_other.data:
                    return False
            else:
                raise ValueError(len_error)
        if probe_other.previous is not other:
            raise ValueError(len_error)
        return True
            
