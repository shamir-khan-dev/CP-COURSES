"""
-------------------------------------------------------
Exam Task 1 Function Definitions: Strings
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-12-05"
-------------------------------------------------------
"""


def longest_string(strings):
    """
    -------------------------------------------------------
    Returns the longest string from the list of strings. If
    multiple strings have the same length, returns the first one.
    If the list is empty, returns an empty string.
    Use: ls = longest_string(strings)
    -------------------------------------------------------
    Parameters:
        strings - a list of strings (list of str)
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        ls - the longest string (str). If no string exists, returns an empty string.
    -------------------------------------------------------
    """

    # your code here
    word = ""
    for x in range(len(strings)):
        if(len(strings[x]) > len(word)):
            word = strings[x]
        
    return word
