"""
-------------------------------------------------------
Midterm AB Task 2 Function Definition
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""


def movie_rating(rating):
    """
    -------------------------------------------------------
    Determines the category of a movie based on its IMDb rating.
        If rating is 9.0 or greater, the category is "Masterpiece".
        If rating is 8.0 or greater but less than 9.0, the category is "Excellent".
        If rating is 7.0 or greater but less than 8.0, the category is "Good".
        If rating is 5.0 or greater but less than 7.0, the category is "Average".
        If rating is 3.0 or greater but less than 5.0, the category is "Below Average".
        If rating is less than 3.0, the category is "Poor".
    Must use a fallthrough algorithm.
    Use: category = movie_rating(rating)
    -------------------------------------------------------
    Parameters:
        rating - movie rating from IMDb (float >= 0)
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        category - description of movie rating category (str)
    -------------------------------------------------------
    """

    # your code here
    
    rate = ""
    
    if(rating<3):
        rate+= "Poor"
    elif(rating >= 3 and rating < 5 ):
        rate+= "Below Average"
    elif(rating >= 5 and rating < 7):
        rate+= "Average"
    elif(rating >= 7 and rating < 8):
        rate+= "Good"
    elif(rating >= 8 and rating < 9):
        rate+= "Excellent"
    elif(rating >= 9):
        rate+= "Masterpiece"
    

    return rate
