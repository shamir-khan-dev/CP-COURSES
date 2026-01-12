"""
-------------------------------------------------------
[Assignment 9, Task 2]
printing positive numbers
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

file_handle = open("numbers.txt", "r", encoding="utf-8")

print(read_integers(file_handle))
