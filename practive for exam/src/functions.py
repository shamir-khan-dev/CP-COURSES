"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-12-10"
-------------------------------------------------------
"""
# Imports

def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    
    line = fh.readline()
    array = []
    while(line != ""):
        lineo = line.strip().split(",")
        if(lineo[0] == id_number):
            array = lineo
            break
        line = fh.readline()

    return array
