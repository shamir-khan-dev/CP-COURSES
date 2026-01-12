"""
-------------------------------------------------------
Testing for Task 7: Files
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      987654321
Email:   ssehra@wlu.ca
__updated__ = "2024-12-09"
-------------------------------------------------------
"""
# Imports
from t07_functions import copy_lines_with_keyword

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')
keyword = 'python'
count = copy_lines_with_keyword(file_input, file_output, keyword)
print(f"{count} lines containing the keyword '{keyword}' have been written to output file.")
file_input.close()
file_output.close()
