"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-01-25"
------------------------------------------------------------------------
"""
# Imports

from utilities import queue_to_array
from Queue_array import Queue

q1 = Queue()

a = []

q1.insert(1)
q1.insert(2)
q1.insert(3)
queue_to_array(q1,a)

print(q1)
print(a)