"""
-------------------------------------------------------
Exam Task 3 Function Definitions: Strings
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-12-05"
-------------------------------------------------------
"""


def valid_product_code(code):
    """
    -------------------------------------------------------
    Determines if a product code is valid based on the following rules:
    - Must be 12 characters long.
    - Starts with 2 uppercase letters.
    - Followed by 4 digits.
    - Followed by 3 letters (uppercase or lowercase).
    - Ends with 3 digits, and their sum is divisible by 5.
    -------------------------------------------------------
    Parameters:
        code - the product code to validate (str)
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        is_valid - True if valid, False otherwise (bool)
    -------------------------------------------------------
    """

    # your code here
    con  = False
    if(len(code) == 12 and code[0:1].isupper() == True and code[1:2].isupper() == True and code[2:6].isdigit() == True and code[6:9].isalpha() == True and (code[9:].isdigit() and code[9:10 ] + code[10:11] + code[11:])//5 == 0):
        con = True
    

    return con
