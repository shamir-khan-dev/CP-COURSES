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
from functions import student_stats

def test_student_stats():
    """
    Test for student_stats function.
    """
    with open("students.txt", "r", encoding="utf-8") as file_handle:
        l_id, h_id, avg = student_stats(file_handle)
        print("Testing student_stats:")
        print(f"Lowest ID: {l_id}, Highest ID: {h_id}, Average Mark: {avg:.2f}")

if __name__ == "__main__":
    test_student_stats()
