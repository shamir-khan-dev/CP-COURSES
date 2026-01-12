"""
-------------------------------------------------------
[Lab 10, Task 4]
finding the first customer 
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports

from functions import customer_first

open_file = open("customers.txt")
print(customer_first(open_file))