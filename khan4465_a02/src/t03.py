"""
-------------------------------------------------------
[Assignment 2, Task 3]
Calculating the date in specified format 
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-29"
-------------------------------------------------------
"""
# Imports

date = int(input("Enter a date in the format YYYYMMDD: "))

year = date // 10000

day = date % 100

month = (date // 100) % 100


print(f"The reformatted date: {year}/{month}/{day}")