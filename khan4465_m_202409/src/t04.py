"""
-------------------------------------------------------
Midterm MC Task 4 Testing
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""
# Imports
from t04_functions import calories_total

meal1 = float(input("Calories for Meal 1: "))
meal2 = float(input("Calories for Meal 2: "))
meal3 = float(input("Calories for Meal 3: "))
print()

# Calculate total and print
total = calories_total(meal1, meal2, meal3)
print()
print(f"calories_total({meal1}, {meal2}, {meal3}) -> Total calories: {total}")
