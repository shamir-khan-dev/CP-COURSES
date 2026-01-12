"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
# Use any appropriate data structure here.
from List_array import List
from pip._internal.operations.install.wheel import rehash

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(List())
    """
    def __str__(self):
        a = []
        if(len(self._table) > 1):
            for x in range(len(self._table)):
                a.append(str(self._table[x]))
                
        return a
    """
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """
        # your code here
        return


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return


    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        # your code here

        hash_value = hash(value)
        index_value = hash_value % self._capacity
        con = False
        if value not in self._table[index_value]:  # Avoid duplicates
            self._table[index_value].append(value)
            con = True
            self._count+=1
        if self._count > (self._LOAD_FACTOR * self._capacity):
            self._rehash()
        return con

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        return

		
    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        val = None
        has_value = hash(key)
        index_value = has_value % self._capacity
        if(key in self._table[index_value]):
            val = key
            self._table[index_value] = None
            self._count-=1
            
        return val


    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        self._capacity = (self._capacity*2) + 1 # Double the capacity

        new_table = [List() for _ in range(self._capacity)]  # New empty table

        for x in range(len(self._table)):  # ✅ Iterate over all slots
            for y in range(len(self._table[x])):  # ✅ Iterate over each element
                hash_value = hash(self._table[x][y])  # Compute new hash
                index_value = hash_value % self._capacity  # Get new index
                if(self._table[x][y] not in new_table[index_value]):
                    new_table[index_value].append(self._table[x][y])  # ✅ Append correctly

        self._table = new_table  # ✅ Update the table reference
        return


    def __eq__(self, target):
        """
        ----------------
        Determines whether two Hash_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a hash set (Hash_Set)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        # your code here
        return


    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        print(f"""{self._capacity} Slots)

----------------------------------------""")
        for x in range(self._capacity):
            print(f"Slot {x}")
            print(f"")
            for y in range(len(self._table[x])):
                print(f"Slot {self._table[x][y]}")

            print(SEP)
        return None

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
