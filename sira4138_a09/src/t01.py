"""
-------------------------------------------------------
Test script for file operations.
-------------------------------------------------------

Author:  Husnain Raja

ID:      169106977

Email:  Raja6977@mylaurier.ca

__updated__ = "2024-11-19"
-------------------------------------------------------
"""

def file_top(file_handle, count):
    """
    Prints the first `count` lines of a file.
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    """
    i = 0
    line = file_handle.readline()
    while i < count and line:
        print(line.strip())  # Print the current line without extra spaces
        i += 1
        line = file_handle.readline()


def test_file_top():
    """
    Test for file_top function.
    Reads and prints the first 5 lines from the file 'students.txt'.
    """
    try:
        # Open the file for reading
        with open("students.txt", "r", encoding="utf-8") as file_handle:
            print("Testing file_top with 5 lines:")
            file_top(file_handle, 5)  # Test the function with 5 lines
    except FileNotFoundError:
        # Handle missing file scenario
        print("Error: The file 'students.txt' does not exist. Please ensure the file is in the correct directory.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the test
    test_file_top()
