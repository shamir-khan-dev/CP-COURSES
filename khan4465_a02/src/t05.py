"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-01-19"
------------------------------------------------------------------------
"""
# Imports
from Movie_utilities import genre_counts

from Movie import Movie

movies = [Movie("Dellamorte Dellamore",1994,"Michele Soavi",10,[7,3,4,5,8]), Movie("Ben 10",1994,"Michele Soavi",9,[7,3,4,5,8]), Movie("Ben 10",1994,"Michele Soavi",10,[7,4,5])]

print(genre_counts(movies))