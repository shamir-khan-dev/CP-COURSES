"""
-------------------------------------------------------
Test script and function definitions for various file operations.
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
    while i < count:
        line = file_handle.readline()
        if not line:  # Stop if the end of the file is reached
            break
        print(line.strip())
        i += 1


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Line numbering starts at 0.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    try:
        i = 0  # Initialize line number
        for line in fh_read:  # Use a for loop for simplicity
            fh_write.write(f"[{i}] {line.strip()}\n")  # Add line number and write
            i += 1  # Increment line number
    except Exception as e:
        print(f"Error during line numbering: {e}")

def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    try:
        for line in file_handle:  # Iterate over lines in the file
            tokens = line.split(",")
            for token in tokens:
                try:
                    number = int(token.strip())
                    if number > 0:
                        number_list.append(number)
                except ValueError:
                    pass  # Ignore non-numeric tokens
    except Exception as e:
        print(f"Error during integer reading: {e}")
    return number_list

def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces, and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = lcount = dcount = wcount = rcount = 0
    try:
        for line in file_handle:  # Iterate over lines
            for char in line:  # Process each character
                if char.isupper():
                    ucount += 1
                elif char.islower():
                    lcount += 1
                elif char.isdigit():
                    dcount += 1
                elif char.isspace():
                    wcount += 1
                else:
                    rcount += 1
    except Exception as e:
        print(f"Error during file statistics calculation: {e}")
    return ucount, lcount, dcount, wcount, rcount

def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    lowest_mark = float("inf")
    highest_mark = float("-inf")
    total_marks = 0
    count = 0
    l_id = h_id = ""

    try:
        for line in file_handle:  # Iterate over lines in the file
            try:
                surname, forename, student_id, mark = line.strip().split(",")
                mark = float(mark)
                total_marks += mark
                count += 1

                if mark < lowest_mark:
                    lowest_mark = mark
                    l_id = student_id
                if mark > highest_mark:
                    highest_mark = mark
                    h_id = student_id
            except ValueError:
                print(f"Skipping malformed line: {line.strip()}")
        avg = total_marks / count if count > 0 else 0  # Avoid division by zero
    except Exception as e:
        print(f"Error during student statistics calculation: {e}")
        avg = 0  # Set average to 0 if there's an error
    return l_id, h_id, avg

if __name__ == "__main__":
    pass  # This script provides functions to be imported and tested
