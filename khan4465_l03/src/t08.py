"""
-------------------------------------------------------
[Lab 3, Task 8]
using f strings with numbers
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-26"
-------------------------------------------------------
"""
# Imports
# user inputs start 
dirt = float(input("Enter amount of dirt (m^3): ")) 
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))
# user inputs end

total = dirt + sand + gravel

print()
print("Material   Cubic Metres")

# condition aligning dirt amount

print(f"Dirt       {dirt:>5.1f}")

# condition aligning gravel amount

print(f"Gravel     {gravel:>5.1f}")

# condition aligning sand amount

print(f"Sand       {sand:>5.1f}")

    
# condition aligning total amount

print(f"Total      {total:>5.1f}")

