"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-08"
-------------------------------------------------------
"""
# Imports
from functions import to_power
# Constants

# Test Cases
test_cases = {
    "to_power(2, 3)": to_power(2, 3),        # 8
    "to_power(-2, 3)": to_power(-2, 3),      # -8
    "to_power(2, -3)": to_power(2, -3),      # 0.125
    "to_power(-2, -3)": to_power(-2, -3),    # -0.125
    "to_power(5, 0)": to_power(5, 0),        # 1
    "to_power(0, 5)": to_power(0, 5),        # 0
    "to_power(0, 0)": to_power(0, 0),        # 1 (by convention)
}

print(test_cases)