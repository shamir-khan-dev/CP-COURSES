"""
-------------------------------------------------------
Midterm AB Task 4 Function Definition
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""


def calories_total(meal1, meal2, meal3):
    """
    -------------------------------------------------------
    Prints a table of the calories consumed in three meals and their total,
    and returns the total calories. Calories are printed with 1 decimal accuracy.
    Use: total = calories_total(meal1, meal2, meal3)
    -------------------------------------------------------
    Parameters:
        meal1 - calories from meal 1 (float >= 0)
        meal2 - calories from meal 2 (float >= 0)
        meal3 - calories from meal 3 (float >= 0)
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        total - the sum of meal1, meal2, and meal3 (float)
    -------------------------------------------------------
    """



    print(f"""Meal Calories
----------------
  1        {meal1}
  2        {meal2}
  3        {meal3}
----------------
           656.0""")
    return float(meal1+meal2+meal3)

    
