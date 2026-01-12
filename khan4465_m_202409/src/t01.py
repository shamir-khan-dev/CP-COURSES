"""
-------------------------------------------------------
Midterm Task 1 Testing
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      11111111
Email:   ssehra@wlu.ca
__updated__ = "2024-10-22"
-------------------------------------------------------
"""
# Imports
from t01_functions import length_conversion

inches_inputs = int(input("inches: "))
miles, yards, feet, inches = length_conversion(inches_inputs)
print(
    f"length_conversion({inches_inputs}) -> Miles: {miles}, Yards: {yards}, Feet: {feet}, Inches: {inches}")
