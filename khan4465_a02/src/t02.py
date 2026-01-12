"""
-------------------------------------------------------
[Assignment 2, Task 2]
Calculating annual task on sales
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-29"
-------------------------------------------------------
"""
# Imports

two_digits = int(input("Enter a positive digit number: "))


first = two_digits // 10
second = two_digits % 10

difference = first - second

print(f"The difference of the digits of {two_digits} is {difference}")