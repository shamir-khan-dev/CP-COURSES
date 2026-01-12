"""
-------------------------------------------------------
[Assignment 9, Task 3]
checks each index for condition
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
# Imports

from functions import file_statistics

file_handle = open("addresses.txt", "r", encoding="utf-8")

print(file_statistics(file_handle))
