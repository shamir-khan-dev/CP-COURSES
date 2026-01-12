"""
-------------------------------------------------------
Testing for Task 5: 2D List
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      987654321
Email:   ssehra@wlu.ca
__updated__ = "2024-12-01"
-------------------------------------------------------
"""
# Imports
from t05_functions import max_row_sum

matrix = [
        [9, -1, 1, -5 ],
        [10, 2, 3, 4],
        [8, 2, 3, 2],
        [-8, 11, 10, 0]
    ]
print("\nMatrix:")
for row in matrix:
    print(row)
max_sum, row_index = max_row_sum(matrix)
print(f"Maximum Row Sum: {max_sum}, Row Index: {row_index}")


max_sum, row_index  = max_row_sum([[-2, 2], [0,0]])

print(f"Maximum Row Sum: {max_sum}, Row Index: {row_index}")


max_sum, row_index  = max_row_sum([])

print(f"Maximum Row Sum: {max_sum}, Row Index: {row_index}")