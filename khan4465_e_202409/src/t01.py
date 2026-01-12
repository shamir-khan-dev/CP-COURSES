"""
-------------------------------------------------------
Testing for Task 1: Strings
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      987654321
Email:   ssehra@wlu.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from t01_functions import longest_string

CASES = [
    [],
    ["apple"],
    ["cat", "dog", "elephant", "mouse"],
    ["banana", "kiwi", "grapefruit", "pear"]
]

for case in CASES:
    print(f'longest_string({case}) -> "{longest_string(case)}"')
    print()
