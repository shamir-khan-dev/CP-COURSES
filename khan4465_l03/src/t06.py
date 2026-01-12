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

from Priority_Queue_array import Priority_Queue
from utilities import pq_to_array

q1 = Priority_Queue()

q1.insert(1)
q1.insert(3)
q1.insert(2)

a = []
print(q1)

print(pq_to_array(q1,a))
print(q1)

print(a)


