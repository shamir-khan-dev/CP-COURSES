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

movie = Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3, 4, 5, 8])
movie_2 = Movie('T1', 2000, 'D1', 5, [0])


print(movie.year)
print(movie.genres_string())
print(movie_2.genres_string())