"""
-------------------------------------------------------
Testing for Task 6: multiply_list
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      987654321
Email:   ssehra@wlu.ca
__updated__ = "2024-12-01"
-------------------------------------------------------
"""
# Imports
from t06_functions import list_common

CASES = (
    ([], [1, 3, 5]),
    ([1, 3, 5], []),
    ([5, 5, 4, 5], [5]),
    ([1, 3, 5, 2, 4, 6, 3, 3], [3, 4]),
)

for master_list, reference_list in CASES:
    print(f"list_common({master_list}, {reference_list}) -> None")
    list_common(master_list, reference_list)
    print(f"  master_list after: {master_list}")
