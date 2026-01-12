"""
-------------------------------------------------------
Circular array version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy




class Queue:
    """
    Circular Array-Based Queue Implementation
    """

    # Default queue size
    DEFAULT_CAPACITY = 10  

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        Initializes an empty queue with a fixed-size list.
        """
        assert capacity > 0, "Queue size must be > 0"

        self._capacity = capacity  # Max size of queue
        self._values = [None] * self._capacity  # Fixed-size list
        self._front = None  # Points to the front element
        self._rear = 0  # Next available slot for insertion
        self._count = 0  # Tracks the number of elements in the queue
    def __str__(self):
        return str(self._values)

    def is_empty(self):
        """
        Determines if the queue is empty.
        """
        return self._count == 0

    def is_full(self):
        """
        Determines if the queue is full.
        """
        return self._count == self._capacity

    def __len__(self):
        """
        Returns the number of elements in the queue.
        """
        return self._count

    def insert(self, value):
        """
        Adds a value to the rear of the queue.
        """
        assert not self.is_full(), "Queue is full"

        # Insert value at the rear position
        self._values[self._rear] = value

        # Move rear forward using circular indexing
        self._rear = (self._rear + 1) % self._capacity

        # If inserting the first element, set _front to 0
        if self._count == 0:
            self._front = 0

        # Increase count
        self._count += 1

    def remove(self):
        """
        Removes and returns the front value of the queue.
        """
        assert not self.is_empty(), "Cannot remove from an empty queue"

        # Get front value
        value = deepcopy(self._values[self._front])

        # Clear the value at the front (optional, for debugging)
        self._values[self._front] = None

        # Move _front forward using circular indexing
        self._front = (self._front + 1) % self._capacity

        # Decrease count
        self._count -= 1

        # Reset _front and _rear if queue becomes empty
        if self._count == 0:
            self._front = None
            self._rear = 0

        return value

    def peek(self):
        """
        Returns the front value without removing it.
        """
        assert not self.is_empty(), "Cannot peek at an empty queue"

        return self._values[self._front]

    def __eq__(self, target):
        """
        Determines whether two Queues are equal.
        """
        if not isinstance(target, Queue) or self._count != target._count:
            return False  # Must be the same type and contain the same number of elements

        for i in range(self._count):
            # Compare values in logical order using circular indexing
            self_value = self._values[(self._front + i) % self._capacity]
            target_value = target._values[(target._front + i) % target._capacity]

            if self_value != target_value:
                return False  # If any value doesn't match, queues are not equal

        return True  # If all values match, queues are equal

    def __iter__(self):
        """
        Generates a Python iterator. Iterates through the queue from front to rear.
        """
        if self._front is not None:
            j = self._front
            for _ in range(self._count):
                yield self._values[j]
                j = (j + 1) % self._capacity  # Move forward using circular indexing
