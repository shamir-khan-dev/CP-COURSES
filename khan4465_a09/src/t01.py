"""
-------------------------------------------------------
[Assignment 9, Task 1]
printing lines
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
# Imports

from functions import file_top
file_handle = open("students.txt", "r", encoding="utf-8")
print(file_top(file_handle,5))