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
from functions import line_numbering

def test_line_numbering():
    """
    Test for line_numbering function.
    """
    with open("wilde.txt", "r", encoding="utf-8") as fh_read:
        with open("wilde_numbered.txt", "w", encoding="utf-8") as fh_write:
            line_numbering(fh_read, fh_write)
    print("Testing line_numbering: Check 'wilde_numbered.txt' for results.")

if __name__ == "__main__":
    test_line_numbering()
