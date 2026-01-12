"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-20"
-------------------------------------------------------
"""
# Imports
from pickle import TRUE, FALSE

def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    
    for x in range(1,len(sentence)):
        if(sentence[x:x+1].isupper() == True):
            sentence = sentence[:x] + " " + sentence[x:]
            sentence = sentence[:x+1] + sentence[x+1:x+2].lower() + sentence[x+2:] 
        
    return sentence

def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    
    if(string[len(string)-1:] == "s" or string[len(string)-2:] == "ch" or string[len(string)-2:] == "sh"):
        string = string + "es"
    if(string[len(string)-1:] == "y"):
        string = string[0:len(string)-1] + "ies"
    else:
        string = string + "s"
    return string

def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    a = ""
    if(str1[len(str1)-3:] == str2[len(str2)-3:]):
        a+=  str1[len(str1)-3:]
    return a

def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    con = False
    if(isbn.isalpha() == False):
        if(len(isbn) == 17):
            if(isbn[0:3] == "978" or isbn[0:3] == "979"):
                if(isbn.count("--") == 0):
                    if(isbn[len(isbn)-2] == "-"):
                        if(isbn.count("-") == 4):
                            con = True
    return con 
                        
def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    fal = 0
    con = True
    for x in range(len(words)-1):
        if(words[x][len(words[x])-1:] == words[x+1][0:1]):
            fal = fal
        else:
            fal+=1
    if(fal > 0):
        con = False
    else:
        con = True 
    return con
            
                    
                        
    
    