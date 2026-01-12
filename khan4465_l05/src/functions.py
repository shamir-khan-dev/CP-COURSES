"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-08"
-------------------------------------------------------
"""
# Imports

# Constants

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    ans = 0
    if(x < 0 or y < 0):
        ans = x - y
    else:
        left = recurse(x - 1, y)
        right = recurse(x, y - 1)
        ans = left + right
        
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    ans = 0
    if(m % n == 0): 
        ans = n
    else:
        ans = gcd(n, m % n)
    return ans

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiouAEIOU"
    total = 0

    if (s == ""):
        total = 0  # Base case: empty string
    else:
        if (s[0] in vowels):  # Check the first character
            total += 1        # Count the vowel
        total += vowel_count(s[1:])  # Add vowels from the rest of the string

    return total

def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power using recursion.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    # Base Case
    ans = 0
    if power == 0:
        ans =  1
    elif power > 0:
        ans =  base * to_power(base, power - 1)  # Recursive case for positive power
    else:
        ans =  1 / to_power(base, -power)        # Recursive case for negative power
    return ans

def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    s = ''.join([char.lower() for char in s if char.isalpha()])

    con = True  # Assume it's a palindrome by default

    # Base Case: Empty string or single character is a palindrome
    if len(s) <= 1:
        con = True
    else:
        # Compare first and last characters
        if s[0] != s[-1]:  # Already in lowercase
            con = False
        else:
            # Recursive call on the substring (without first and last characters)
            con = is_palindrome(s[1:-1])

    return con

def bag_to_set(bag, seen=None):
    if seen is None:
        seen = []

    if bag:
        if bag[0] not in seen:
            seen.append(bag[0])
        bag = bag[1:]

    return bag_to_set(bag, seen) if bag else seen

