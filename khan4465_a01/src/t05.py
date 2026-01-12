"""
-------------------------------------------------------
Assignment 1, Task 5
Calculating Interest rate
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-22"
-------------------------------------------------------
"""
# Imports

principal = float(input("Please enter the principal amount: "))
interest = float(input("enter the interest rate: "))/100
number_of_years = int(input("enter the years: "))
interest_compounded_per_year = int(input("enter the years for compound: "))

amount = principal * (1 + interest / interest_compounded_per_year) ** (interest_compounded_per_year * number_of_years)

# Print the result with two decimal places
print(f"Balance: $ {amount:.10f}")