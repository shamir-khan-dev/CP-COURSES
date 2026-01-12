"""

-------------------------------------------------------

[program description]

-------------------------------------------------------

Author:  Bazif Siraj

ID:      169094138

Email:  sira4138@mylaurier.ca

__updated__ = "2024-11-17"

-------------------------------------------------------

"""
from functions import file_statistics

def test_file_statistics():
    """
    Test for file_statistics function.
    """
    with open("addresses.txt", "r", encoding="utf-8") as file_handle:
        ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
        print("Testing file_statistics:")
        print(f"Uppercase: {ucount}, Lowercase: {lcount}, Digits: {dcount}, Whitespace: {wcount}, Other: {rcount}")

if __name__ == "__main__":
    test_file_statistics()
