"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
# Imports

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    
    total_lines = len(file_handle.readlines())
    file_handle.seek(0)
    line = file_handle.readline()
    num = 0
    if(count > total_lines):
        
        while(line != ""):
            print(line.strip())
            line = file_handle.readline()
    else:
        while(num < count):
            print(line.strip())
            line = file_handle.readline()
            num+=1

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
    
    line = file_handle.readline().strip()
    each_index = line.split(",")
    postive_numbers = []
    while(line != ""):
        if(int(each_index[1]) > 0):
           postive_numbers.append(int(each_index[1]))
        if(int(each_index[2]) > 0):
           postive_numbers.append(int(each_index[2]))
        if(int(each_index[3]) > 0):
           postive_numbers.append(int(each_index[3]))
        line = file_handle.readline().strip()
    return postive_numbers
            
def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
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
    
    line = file_handle.readline()
    
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    
    while(line != ""):
        for x in range(len(line)):
            if(line[x].isupper() == True):
               ucount+=1
            elif(line[x].islower() == True):
               lcount+=1
            elif(line[x].isdigit() == True):
               dcount+=1
            elif(line[x].isspace() == True):
               wcount+=1
            else:
                rcount+=1
        line = file_handle.readline()
    return ucount,lcount,dcount,wcount,rcount

def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    
    line = fh_read.readline()
    num = 0
    while(line != ""):
        fh_write.write(f"[{num}] {line}")
        num+=1
        line = fh_read.readline()
    return None

def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
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
    
    
    total_lines = file_handle.readline()
    
    lowest_mark = 100
    highest_mark = 0
    highest_mark_id = 0
    lowest_mark_id = 0
    
    t = 0
    while(total_lines != ""):
        total_lines = total_lines.split(",")
        if(int(total_lines[3]) > highest_mark):
            highest_mark = int(total_lines[3])
            highest_mark_id = total_lines[2]
        total_lines = file_handle.readline()
     
    while(total_lines != ""):
        total_lines = total_lines.split(",")
        if(int(total_lines[3]) < lowest_mark):
            lowest_mark = int(total_lines[3])
            lowest_mark_id = total_lines[2]
        total_lines = file_handle.readline()
    while(total_lines != ""):
        total_lines = total_lines.split(",")
        t +=  total_lines[3].strip()
 
    return highest_mark_id,lowest_mark_id,t/9
        
            
            

               
             
        