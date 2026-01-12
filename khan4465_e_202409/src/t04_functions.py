"""
-------------------------------------------------------
Exam Task 4 Function Definitions: File and 2D list
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-12-09"
-------------------------------------------------------
"""


def file_to_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = file_to_matrix(fh_in)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    # your code here
    start = 0
    a = []
    line = fh_in.readline()
    for x in range(rows):
        array = []
        for y in range(start,cols):
            array.append(line[y])

        line = fh_in.readline()
        a.append(array)

    return a
