"""
-------------------------------------------------------
Testing for Task 3: Strings
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      987654321
Email:   ssehra@wlu.ca
__updated__ = "2024-12-05"
-------------------------------------------------------
"""
# Imports
from t03_functions import valid_product_code
PRODUCT_CODES = [
    "AB1234XYZ055",  # Valid
    "AB1234xyz055",  # Valid
    "AB123XYZ0055",   # Invalid (too short)
    "ab1234XYZ055",  # Invalid (lowercase start)
    "AB1234XYZ015",  # Invalid (last three digits sum not divisible by 5)
    "AB1234X1Z015",  # Invalid (letters replaced by a digit in middle)
]

print("Product Code Validation:")
for code in PRODUCT_CODES:
    print(f"Code: {code} -> Valid: {valid_product_code(code)}")
