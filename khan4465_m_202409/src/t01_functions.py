"""
-------------------------------------------------------
Midterm AB Task 1 Function Definitions
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""
# Constants

# your constants here


def length_conversion(total_inches):
    """
    -------------------------------------------------------
    Breaks down total inches into miles, yards, feet, and inches.
    The change can be:
        miles - converted from 63360 inches
        yards - converted from 36 inches
        feet - converted from 12 inches
        inches -  left over inches
    Use: miles, yards, feet, inches = length_conversion(total_inches)
    -------------------------------------------------------
    Parameters:
        total_inches - total length in inches (int >= 0)
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        miles - number of full miles (int)
        yards - number of full yards (int)
        feet - number of full feet (int)
        inches - number of remaining inches (int)
    -------------------------------------------------------
    """
    m = int(total_inches/63360)
    y = int(total_inches/36)
    f = int(total_inches/12)
    i = total_inches-(m+y+f)
    # your code here
    
    

    return m,y,f,i
