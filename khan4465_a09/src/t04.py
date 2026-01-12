"""
-------------------------------------------------------
[Assignment 9, Task 4]
adding numbers to line
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
# Imports

from functions import line_numbering

file_handle = open("wilde.txt", "r", encoding="utf-8")
file_handle_one = open("wilde_numbered.txt", "a", encoding="utf-8")
print(line_numbering(file_handle,file_handle_one))


