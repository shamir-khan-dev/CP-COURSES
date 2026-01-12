"""
-------------------------------------------------------
[Lab 3, Task 5]
user input diffrence numbers
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-25"
-------------------------------------------------------
"""
# Imports

mins = int(input("Enter minimum: "))
maxs = int(input("Enter maximum: "))

len_max = len(str(maxs)) + 2
len_min = len(str(mins)) + 2

diff = maxs - mins
len_diff = len(str(diff)) + 1
print(f"The difference between{maxs:^{len_max}}and{mins:^{len_min}}is{diff:>{len_diff}}")
