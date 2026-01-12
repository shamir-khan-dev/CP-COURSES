"""
-------------------------------------------------------
[Lab 8,functions]
function which does various operations
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-08"
-------------------------------------------------------
"""
# Imports

from random import randint

def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    integer_list = []
    for i in range(n):
        integer_list.append(randint(low,high))
    return integer_list

def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    
    total_negatives = 0
    total_positives = 0
    total_zeroes = 0
    total_evens = 0
    total_odds = 0
    
    for x in range(len(values)):
        if(values[x] == 0):
            total_zeroes+=1
        if(values[x]%2 == 0):
           total_evens+=1
        else:
             total_odds+=1
        if(values[x] > 0):
            total_positives+=1
        if(values[x] < 0):
            total_negatives+=1
    return total_negatives,total_positives,total_zeroes,total_evens,total_odds
            
def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    
    index_list = []
 
    for x in range(len(values)):
        if(value == values[x]):
            index_list.append(x)
    return index_list


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the union of source1 and source2 (list of *)
    -------------------------------------------------------
    
    """
    target = []
    for item in source1:
        if(item not in target):
            target.append(item)
    for item in source2:
        if(item not in target):
            target.append(item)
    return target

def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    for item in source1:
        if(item not in target and item not in source2):
            target.append(item)
    for item in source2:
        if(item not in target and item not in source1):
            target.append(item)
            
            
    return target
            
    