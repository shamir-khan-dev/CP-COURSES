"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-01-16"
------------------------------------------------------------------------
"""
# Imports

from Movie import Movie

m1 = Movie('T1', 2000, 'D1', 5, [0])

m2 = Movie('T1', 2000, 'D1', 5, [3, 4, 5, 8])


print(m1.genres_list_string())
print(m2.genres_list_string())

