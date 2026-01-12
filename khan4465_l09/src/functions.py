"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-03-15"
-------------------------------------------------------
"""
# Imports

# Constants

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("""Hashes
Hash     Slot Key
-------- ---- --------------------
""")

    hash_value = 0
    index_value = 0 
    for x in range(len(values)):
        hash_value = hash(values[x])
        index_value = hash_value % slots
        print(f"{hash_value:<8} {index_value:<4} {values[x]}")    
    print("...")
    return None
    