"""
-------------------------------------------------------
Array version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy
from pickle import FALSE


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []
    
    def __str__(self):
        return str(self._values)

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """

        # Your code here
        i = 0
        while i < len(self._values):
            if self._values[i] == key:
                return True
            i += 1
        return False

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        
        copy =  deepcopy(self._values[i])
        return copy


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        return len(self._values)

        return

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Your code here
    
        low = 0
        high = len(self._values) - 1

        while(low < high):
            
            mid = (low + high) // 2

            if key > self._values[mid]:
            # Key is greater, search the right half
                low = mid + 1
            else:
            # Search the left side even if equal (to find the FIRST occurrence)
                high = mid

        # Deferred equality check
        if low == high and self._values[low] == key:
            return low
        else:
            return -1
    
    def _binary_search_to_the_right(self, key):
        """
        -------------------------------------------------------
        Searches for the last occurrence of key in the sorted list.
        Performs a stable search to find the rightmost (last) occurrence.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search_to_the_right(key)
        -------------------------------------------------------
        Parameters:
        key - a data element (?)
        Returns:
        i - the index of the last occurrence of key in
            the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        low = 0
        high = len(self._values) - 1
        result = -1  # To store the index of the last occurrence if found

        while low <= high:
            mid = (low + high) // 2

            if key < self._values[mid]:
                # Search the left half
                high = mid - 1
            elif key > self._values[mid]:
                # Search the right half
                low = mid + 1
            else:
                # Found a match; move right to find the last occurrence
                result = mid
                low = mid + 1  # Keep searching to the right

        return result


    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # Your code here
        new_list = []
        i = 0
        while i < len(self._values):
            if self._values[i] not in new_list:
                new_list.append(self._values[i])
            i += 1
        self._values = new_list
        return None


    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        # Your code here
        count = 0
        i = 0
        while i < len(self._values):
            if self._values[i] == key:
                count += 1
            i += 1
        return count
    
    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # Your code here
        i = 0
        found = None
        while i < len(self._values) and found is None:
            if self._values[i] == key:
                found = deepcopy(self._values[i])
            i += 1
        return found

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        # Your code here
        i = 0
        index = -1
        while i < len(self._values) and index == -1:
            if self._values[i] == key:
                index = i
            i += 1
        return index
    

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        i = 0
        while i < len(self._values):
            if value < self._values[i]:
                self._values.insert(i, value)
                return
            i += 1
        self._values.append(value)
        
    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0
        while i < len(source1._values):
            if source1._values[i] in source2._values and source1._values[i] not in self._values:
                self._values.append(source1._values[i])
            i += 1
        return None
    
    def max(self):
        assert len(self._values) > 0, 'Cannot find maximum of an empty list'
        return deepcopy(self._values[-1])

    def min(self):
        assert len(self._values) > 0, 'Cannot find minimum of an empty list'
        return deepcopy(self._values[0])
    
    
    def peek(self):
        assert len(self._values) > 0, 'Cannot peek at an empty list'
        return deepcopy(self._values[0])

    def remove(self, key):
        index = self.index(key)
        return self._values.pop(index) if index != -1 else None

    def remove_front(self):
        assert len(self._values) > 0, 'Cannot remove from an empty list'
        return self._values.pop(0)

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here
        return len(self._values) == 0


    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (Sorted_Lists)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # Your code here
        
        con = False
        if(len(self._values) == len(target._values)):
            i = 0
            total = 0
            while(i != len(self._values)):
                if(self._values[i] == target._values[i]):
                    total+=1
                i+=1
            if(total == len(self._values)):
                con = True
        return con

    

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise 
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

   

   

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        # Your code here
        i = 0
        while i < len(self._values):
            if self._values[i] == key:
                self._values.pop(i)
            else:
                i += 1
        return None
    
    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here

        mid = (len(self._values) + 1) // 2  # Ensures the first half gets more in case of an odd length
        target1 = Sorted_List()
        target2 = Sorted_List()
        target1._values = self._values[:mid]
        target2._values = self._values[mid:]
        self._values = []
        return target1, target2
    
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here
        target1 = Sorted_List()
        target2 = Sorted_List()
        i = 0
        while len(self._values) > 0:
            target1._values.append(self._values.pop(0))
            if len(self._values) > 0:
                target2._values.append(self._values.pop(0))
        return target1, target2
    
    
    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        i = 0
        while i < len(self._values):
            if func(self._values[i]):
                target1._values.append(self._values[i])
            else:
                target2._values.append(self._values[i])
            i += 1
        self._values = []
        return target1, target2

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here
        target1 = Sorted_List()
        target2 = Sorted_List()
        i = 0
        while i < len(self._values):
            if self._values[i] < key:
                target1._values.append(self._values[i])
            else:
                target2._values.append(self._values[i])
            i += 1
        self._values = []
        return target1, target2


    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        i = 0
        while i < len(source1._values):
            if source1._values[i] not in self._values:
                self._values.append(source1._values[i])
            i += 1
        j = 0
        while j < len(source2._values):
            if source2._values[j] not in self._values:
                self._values.append(source2._values[j])
            j += 1
        return None

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

