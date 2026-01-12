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

from functions import stack_split_alt

s1 = Stack()

num = [8,14,12,9,8,7,5]

for x in range(len(num)):
    s1.push(num[x])
    
#print(s1)

print(stack_split_alt(s1))