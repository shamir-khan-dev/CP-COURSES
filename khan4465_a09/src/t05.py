"""
-------------------------------------------------------
[Assignment 9, Task 5]
adding numbers to line
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
# Imports

from functions import student_stats

file_handle = open("students.txt", "r", encoding="utf-8")

print(student_stats(file_handle))