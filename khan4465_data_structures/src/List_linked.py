"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-06-10"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        
        return self._count == 0
    def __str__(self):
        result = ""
        if(self._count == 0):
            result+= "[]"
        else:
            result+="["
            
            current_node = self._front
            while(current_node is not None):
                if(current_node._next is not None):
                    result += str(current_node._value) + ","
                else:
                    result += str(current_node._value)
                current_node = current_node._next
            result += "]"
        return result + "length: " + str(self._count)

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        new_node = _List_Node(value,self._front)
        
        if(self._front is None):
            self._front = new_node
            self._rear = new_node
        else:
            self._front = new_node
        self._count+=1
        
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        new_node = _List_Node(value, None)
        
        if(self._rear is None):
            self._rear = new_node
            self._front = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count+=1
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        
        if(i >= self._count):
            self.append(value)
            
        elif(i <= 0):
            self.prepend(value)
        else:
            current_node = self._front
            for x in range(i-1):
                current_node = current_node._next
            new_node = _List_Node(value,current_node._next)
            current_node._next = new_node
            self._count+=1
        
        return 

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key is not found (int)
        -------------------------------------------------------
        """
        # your code here
        previous_node = None
        current_node = self._front 
        index_count = 0
        
        while(current_node is not None and current_node._value != key):
            previous_node =  current_node
            current_node = current_node._next
            index_count+=1
            
        if(current_node is None):
            index_count = -1 
       
        return previous_node, current_node, index_count

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        
        previous, current, index_i = self._linear_search(key)
        
        value = None
        
        if(index_i == 0):
            value = self._front._value
            self._front = current._next
            if(self._front is None):
                self._rear = None
            self._count-=1
            
        elif(index_i == self._count - 1 and current is not None):
            value = self._rear._value
            if(self._count - 1 == 0):
                self._rear = None
                self._front = None
            else:
                previous._next = None
                self._rear = previous
            self._count-=1
            
        elif(index_i > 0 and index_i < self._count - 1):
            value = current._value      
            previous._next =  current._next
            self._count-=1
        
            
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        # your code here
        
        if(self._front is not None):
            value = self._front._value
        
            if(self._front._next is None):
                self._rear = None
            
            self._front = self._front._next
            self._count-=1
        
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        while current is not None:
            if current._value == key:
                if previous is None:
                    self._front = current._next
                    if self._front is None:
                        self._rear = None
                    current = self._front
                else:
                    previous._next = current._next
                    if current._next is None:
                        self._rear = previous
                    current = current._next
                self._count -= 1
            else:
                previous = current
                current = current._next
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        value = None
        
        result = self._linear_search(key)
        
        if(result[1] is not None):
            value = deepcopy(result[1]._value)
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        # your code here
        
        value = None
        
        if(self._front is not None):
            value = deepcopy(self._front._value)
            
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        # your code here
        index_key = self._linear_search(key)
        
        return index_key[2]

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        
        if(i >= 0):
            
            current_node = self._front
            
            for x in range(i):
                current_node = current_node._next 
        else:
            
            i = (self._count) + i
            
            current_node = self._front
            
            for x in range(i):
                current_node = current_node._next 
        
        return deepcopy(current_node._value)

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        current_node = self._front
        
        for x in range(i - 1):
            current_node = current_node._next
        
        if(i == 0):
            new_node = _List_Node(value, current_node._next)
            self._front = new_node      
        else:
           new_node = _List_Node(value, current_node._next._next)
           current_node._next = new_node
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        
        result = self._linear_search(key)
        con = False
        
        if(result[1] is not None):
            con = True
        
        return con

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        max_num = self._front._value
        current_node = self._front
        
        while(current_node is not None):
            if(current_node._value > max_num):
                max_num = current_node._value
            current_node = current_node._next
        return deepcopy(max_num)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        min_num = self._front._value
        current_node = self._front
        
        while(current_node is not None):
            if(current_node._value < min_num):
                min_num = current_node._value
            
            current_node = current_node._next

        return deepcopy(min_num)

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        # your code here
        total = 0
        current_node = self._front
        
        while(current_node is not None):
            if(current_node._value == key):
                total+=1
            current_node = current_node._next
        
        return total

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        
        
        if(self._front is not None):
            
            previous_node = self._front
            current_node = self._front._next
            
            while(current_node is not None):
            
                if(previous_node._value == current_node._value):
                    previous_node._next = current_node._next  
                    current_node = current_node._next
                    self._count-=1
                else:
                    previous_node = previous_node._next
                    current_node = current_node._next
            if(self._count == 1):
                self._front = self._rear 
            
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        total = 0
        con = False
        
        if(self._count == target._count):
            
            current_node = self._front
            target_node = target._front
            
            
            while(current_node is not None and target_node is not None):
                
                if(current_node._value == target_node._value):
                    total+=1
                current_node = current_node._next
                target_node = target_node._next
        
        if(total == self._count):
            
            con = True 
        
        return con

    def identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        # your code here
        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        mid = (self._count + 1) // 2
        i = 0
        current = self._front
        while i < mid:
            target1.append(current._value)
            current = current._next
            i += 1
        while current is not None:
            target2.append(current._value)
            current = current._next
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True
        current = self._front
        while current is not None:
            if left:
                target1.append(current._value)
            else:
                target2.append(current._value)
            left = not left
            current = current._next
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        # your code here
        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        # your code here
        return
    
    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if(source1._front is not None and source2._front is not None):
            
            current_node_source1 = source1._front
            current_node_source2 = source2._front
                        
            if(source1._count >= source2._count):
            
                while(current_node_source2 is not None):
                
                    if(current_node_source2._value in source1 and current_node_source2._value not in self):
                        self.append(deepcopy(current_node_source2._value))
                
                    current_node_source2 = current_node_source2._next
        
            else:
                 while(current_node_source1 is not None):
                
                    if(current_node_source1._value in source2 and current_node_source1._value not in self):
                        self.append(deepcopy(current_node_source1._value))
                
                    current_node_source1 = current_node_source1._next
        
        return None
    

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current1 = source1._front
        while current1 is not None:
            if current1._value not in self:
                self.append(current1._value)
            current1 = current1._next
        current2 = source2._front
        while current2 is not None:
            if current2._value not in self:
                self.append(current2._value)
            current2 = current2._next
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        
        new_node = _List_Node(source._front._value, self._front)
        
        if(self._count == 0):
            self._front = new_node
            self._rear = new_node
            self._count+=1
        else:
            self._front = new_node
            self._count+=1
            
        if(source._front._next is None):
            source._rear = source._front
        
        source._front = source._front._next
        
        source._count-=1
        
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        if(source._front is not None):
            new_node =  _List_Node(source._front._value, None)
        
            if(self._count == 0):
            
                self._front = new_node
                self._rear = new_node
                self._count+=1
            else:
                self._rear._next = new_node
                self._rear =  new_node
                self._count+=1
        
            if(source._front._next is None):
                source._rear = None
                   
            source._front = source._front._next
        
            source._count-=1

        return 

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        
        
        while(source1._front is not None and source2._front is not None):
            self._move_front_to_rear(source1)
            self._move_front_to_rear(source2)
            
           
        
        while(source1._front is not None):
            self._move_front_to_rear(source1)

        
        while(source2._front is not None):
            self._move_front_to_rear(source2)

        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next