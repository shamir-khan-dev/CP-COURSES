"""
-------------------------------------------------------
[Assignment 2, Task 1]
Calculating annual task on sales
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-29"
-------------------------------------------------------
"""
# Imports

ANNUALTAX = 18.5/100

sales_amount = int(input("Enter the total sales: $"))

toal = ANNUALTAX * sales_amount

print(f'''Projected Tax Report
--------------------------
Total sales:   $ {sales_amount}
Annual tax:    % 18.5
--------------------------
Tax:           $  {toal} ''')