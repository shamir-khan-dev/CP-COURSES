"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-12-10"
-------------------------------------------------------
"""
# Imports

from functions import customer_by_id

file = open("customers.txt","r")

print(customer_by_id(file,"23456"))