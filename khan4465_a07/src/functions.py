"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-09"
-------------------------------------------------------
"""
# Imports
from pickle import NONE
def list_factors(number):
    """
    -------------------------------------------------------
    returns the factors of a number    
    Use: result = list_factors()
    -------------------------------------------------------
    Parameters:
    numbers - (int > 0)

    Returns:
        list of factors of the number - (int > 0)
    ------------------------------------------------------
    """
    factors = []
    for x in range (1,number):
        if((number % x) == 0):
            factors.append(x)
    return factors

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    user_list = []
    user_input = int(input("Enter a positive number: "))
    while(user_input!=0):
        if(user_input>0):
            user_list.append(user_input)
        user_input = int(input("Enter a positive number: "))
    return user_list

def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    targets_index = []
    
    for x in range(len(numbers)):
        if(target_number == numbers[x]):
            targets_index.append(x)
    return targets_index

def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for item in subtrahend:
        while item in minuend:
            minuend.remove(item)
    return None

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    if(len(numbers) == 0):
        return True, -1
    for x in range(len(numbers)):
        if(numbers[x]<numbers[x+1]):
            return True, -1
        else:
            return True, 
                      
                


    