"""
-------------------------------------------------------
[Lab 10, Task 10]
finding the word
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word

open_file = open("words.txt","r")

print(count_frequency_word(open_file,"Exercise"))
