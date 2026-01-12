"""

-------------------------------------------------------

[program description]

-------------------------------------------------------

Author:  Husnain Raja

ID:      169106977

Email:  Raja6977@mylaurier.ca

__updated__ = "2024-11-19"
-------------------------------------------------------

"""
from functions import read_integers

def test_read_integers():
    """
    Test for read_integers function.
    """
    with open("numbers.txt", "r", encoding="utf-8") as file_handle:
        result = read_integers(file_handle)
        print("Testing read_integers:")
        print("Extracted integers:", result)

if __name__ == "__main__":
    test_read_integers()
