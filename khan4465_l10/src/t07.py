"""
-------------------------------------------------------
[Lab 10, Task 7]
finding the maximum number
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num
open_file = open("numbers.txt.","r+")
print(append_max_num(open_file))