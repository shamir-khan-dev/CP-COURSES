"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-01-26"
------------------------------------------------------------------------
"""
# Imports

from Stack_array import Stack

from functions import stack_reverse

s1 = Stack()

for x in range(10):
    s1.push(x)
    
print(s1)

print(stack_reverse(s1))

print(s1)