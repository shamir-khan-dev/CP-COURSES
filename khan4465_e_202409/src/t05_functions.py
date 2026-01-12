"""
-------------------------------------------------------
Exam Task 5 Function Definitions: 2D List
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-12-05"
-------------------------------------------------------
"""


def max_row_sum(matrix):
    """
    -------------------------------------------------------
    Finds the maximum sum of a row and its index in a square matrix.
    If there are multiple rows with the same maximum sum, the index
    of the first such row is returned.
    Use: max_sum, row_index = max_row_sum(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
            Assumes the matrix is square (number of rows equals the number of columns).
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        max_sum - the maximum row sum (int)
        row_index - the index of the row with the maximum sum (int)
            Returns -1 if the matrix is empty.
    -------------------------------------------------------
    """

    # your code here
    sum = 0
    index = 0
    sum_one = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            sum_one+=matrix[x][y]
        if(sum_one>sum):
            sum = sum_one
            index = x

        
    return sum,index
