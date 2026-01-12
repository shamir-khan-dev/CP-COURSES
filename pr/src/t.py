"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-12"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
s1 = Stack()
a = "sha|mir"
for x in range((len(a)//2)+1,len(a)):
    s1.push(a[x])
print(s1)