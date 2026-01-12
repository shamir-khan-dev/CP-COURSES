"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-01-18"
------------------------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_to_array
stack = Stack()
new = []
for x in range(10):
    stack.push(x)
    
print(stack_to_array(stack,new))

print(new)