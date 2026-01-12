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

from Movie_utilities import get_by_year

from Movie import Movie

movies = [Movie("Dellamorte Dellamore",1994,"Michele Soavi",10,[7.2,3,4,5,8]), Movie("Ben 10",1994,"Michele Soavi",10,[7.2,3,4,5,8]), Movie("Ben 10",1994,"Michele Soavi",10,[7.2,3,4,5,8])]

a = get_by_year(movies,1994)

print(a)

#print(movies[0])

