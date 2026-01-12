"""
-------------------------------------------------------
Testing for Task 4: File and 2D list
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      987654321
Email:   ssehra@wlu.ca
__updated__ = "2024-12-01"
-------------------------------------------------------
"""
# Imports

from t04_functions import file_to_matrix

CASES = (
    ("numbers.txt", 2, 2),
    ("numbers.txt", 5, 3),
    ("numbers.txt", 6, 8),
)

for case in CASES:
    f_in = open(case[0], "r", encoding="utf-8")
    matrix = file_to_matrix(f_in, case[1], case[2])
    print(f'file_to_matrix(f_in, {case[1]}, {case[2]})  ->')
    print(matrix)
    f_in.close()
    print()

