"""
-------------------------------------------------------
[Lab 9,functions]
function which does various operations
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-15"
-------------------------------------------------------
"""
# Imports
from pickle import TRUE

def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    hydroxide = False
    if(chemical[len(chemical)-2:len(chemical)] == "OH"):
        hydroxide = True 
    
    return hydroxide

def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    return product_code[0:3],product_code[3:7],product_code[7:]

def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0
    new = s.lower()
    for x in range(len(new)):
        if(new[x:x+1] == "a" or new[x:x+1] == "e" or new[x:x+1] == "i" or new[x:x+1] == "o" or new[x:x+1] == "u"):
            count+=1
    return count

def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    
    for char in txt:
        if (char.isupper()):
            uppr+=1
        if (char.islower()):
            lowr+=1
        if (char.isdigit()):
            dgts+=1
        if (char.isspace()):
            whtspc+=1
    return uppr,lowr,dgts,whtspc

def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    distance = 0
    if(s1 == s2):
        distance = 0
    if(len(s1) != len(s2)):
        distance = -1
    
    if(len(s1) == len(s2)):
        for x in range(len(s1)):
            if(s1[x:x+1] != s2[x:x+1]):
                distance+=1
    return distance
            
                         
    
        

        
        