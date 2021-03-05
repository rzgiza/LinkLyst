class Node(object):
    """
    Creates a node object to store data and point to the next node. Default 
    parameters are used to create an empty header node. Use Node() to 
    instantiate the empty header node before populating with data
    via the insert method. Inserting data will result in the creation of an
    iterable structure collectivley refered to as a singly linked list. Methods
    are defined to allow for the removal of data by index (pop) or by 
    specifying a target item (remove). Getting and setting data by indexing is 
    also supported.
    """
        
    def __init__(self, data=None, next_=None):
        """Creates node object."""
        self.data = data
        self._size = 0
        if next_ is None:
            self.next_ = self
        else:
            self.next_ = next_
            
    def __len__(self):
        """-> size of linked list. Size is defined to be number of nodes
        in the structure excluding the empty header node."""
        return self._size
    
    def size_inc(self):
        """Increase size of linked list by 1."""
        self._size += 1
        
    def size_dec(self):
        """Decrease size of linked list by 1."""
        self._size -= 1
    
    def __iter__(self):
        """Allows for iteration through the linked list's data by traversing 
        the sequential nature of the data structure. Excludes data from header
        node."""
        probe = self
        while probe.next_ is not self:
            probe = probe.next_
            yield probe.data
            
    def __str__(self):
        """-> string representation of the linked structure."""
        return "[" + ", ".join(map(repr, self)) + "]"
        
    def insert(self, item, index=None):
        """Insert data method which creates a linked list of nodes. Index must 
        be within range, with default index of 0."""
        if index is None:
            index = 0
        if index >= 0 and index <= len(self):
            probe = self
            while index > 0 and probe.next_ is not self:
                probe = probe.next_
                index -= 1
            probe.next_ = Node(item, probe.next_)
            self.size_inc()
        else:
            raise IndexError("Index Outside of Bounds: 0 <= index <= len(Node).")
        
    def pop(self, index=None):
        """Remove data method from linked list of nodes by index. 
        -> removed data. Index must be within range, with default index 
        of 0."""
        if len(self) == 0:
            raise IndexError("len(Node) = 0. No item to pop in empty node.")
        if index is None:
            index = 0
        if index >= 0 and index < len(self):
            probe = self 
            while index > 0 and probe.next_.next_ is not self:
                probe = probe.next_
                index -= 1
            removed_data = probe.next_.data
            probe.next_ = probe.next_.next_
            self.size_dec()
            return removed_data
        else:
            raise IndexError("Index Outside of Bounds: 0 <= index < len(Node).")
            
    def remove(self, target_item):
        """Remove data method from linked list of nodes by specifying target
        item."""
        if len(self) == 0:
            raise IndexError("len(Node) = 0. No item to remove in empty node.")
        probe = self
        while probe.next_.next_ is not self:
            if probe.next_.data == target_item:
                break
            probe = probe.next_
        if probe.next_.data == target_item:
            probe.next_ = probe.next_.next_
            self.size_dec()
            return True
        else:
            return False
    
    def __getitem__(self, index):
        """-> data at specified index. Index must be within range."""
        if len(self) == 0:
            raise IndexError("len(Node) = 0. Cannot index.")
        if index >= 0 and index < len(self):
            probe = self
            while index >= 0 and probe.next_ is not self:
                probe = probe.next_
                index -= 1
            return probe.data
        else:
            raise IndexError("Index outside of bounds: 0 <= index < len(Node).")
    
    def __setitem__(self, index, new_item):
        """Overwrite existing data with a new item at a specified index. Index
        must be within range."""
        if len(self) == 0:
            raise IndexError("len(Node) = 0. Cannot index.")
        if index >= 0 and index < len(self):
            probe = self
            while index >= 0 and probe.next_ is not self:
                probe = probe.next_
                index -= 1
            probe.data = new_item
        else:
            raise IndexError("Index outside of bounds: 0 <= index < len(Node).")
    
    def __eq__(self, other):
        """Test for equality between a linked list of nodes and another object.
        If the other object is found to be a linked list of nodes of the same 
        size, then the equality check will ensure data is not obscured by user
        perturbation of the size attribute for either operand."""
        if self is other:
            return True
        elif (type(self) is type(other)) and (len(self) == len(other)):
            len_error = "len(self) = len(other) but strucutres do not match. "\
            "Check <instance>._size for error or broken links."
            probe_self = self
            probe_other = other
            while probe_self.next_ is not self:
                if probe_other.next_ is not other:
                    probe_self = probe_self.next_
                    probe_other = probe_other.next_
                    if probe_self.data != probe_other.data:
                        return False
                else:
                    raise ValueError(len_error)
            if probe_other.next_ is not other:
                raise ValueError(len_error)
            return True
        else:
            return False
    

    
