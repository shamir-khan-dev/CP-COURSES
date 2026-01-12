"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports

# Constants

from List_array import List
from utilities import list_to_array
from utilities import list_test


lisk = []

s1 = List()

for x in range(10):
    s1.insert(x, x)
    
print(s1)

print(list_to_array(s1,lisk))

print(list_test(lisk))

