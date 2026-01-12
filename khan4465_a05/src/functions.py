"""
-------------------------------------------------------
[Assignment 5,functions]
function which does various operations
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-10-27"
-------------------------------------------------------
"""
# Imports

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    total = 1
    for x in range(2,number+1):
        total*= x  
    return total
        
def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates calories burned per minute for total minutes.
    Use: cal = calories_treadmill(number,number)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (int > 0)
        minutes - total time of workout (int > 0)
    Returns:
        calories burned per five minutes of minutes 
    ------------------------------------------------------
    """
    for x in range(5,minutes+5,5):
        cal = float(per_min*x)
        print(f"{x:>2}{cal:>6.1f}")


def arrow_up(rows):
    """
    -------------------------------------------------------
    Draws "#" in the shape of a tree
    Use: tree = arrow_up(4) (int > 0)
    -------------------------------------------------------
    Parameters:
        rows - the height of the tree (int>0)
    Returns:
        the tree
    ------------------------------------------------------
    """
    a = "#"
    b = " "
    for x in range(0,rows):
        if(x <=0):
            print(f"{a:>{rows-x}}")
        else:
            print(f"{a:>{rows-x}}{a:>{x*2}}")
    return None
        
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    a =" "*12
    b = "-"*8
    for x in range(start_num,stop_num+1):
        print(f"""{a}{x:>5}
       {b+5}
        {b} |    4    6    8""")

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = start
    for x in range(start,(count*increment),increment):
        total=total + x+increment
    return total
        
        

        