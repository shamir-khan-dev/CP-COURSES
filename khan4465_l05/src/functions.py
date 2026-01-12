"""
-------------------------------------------------------
[Lab 5,functions]
function which does various operations
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-10-11"
-------------------------------------------------------
"""
# Imports
import math


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    ACCLERATION = 9.8 
    weight = (ACCLERATION * mass)
    final = ""
    if(weight>1000):
        final = weight,'heavy'
    elif(weight<10):
        final = weight,'light'
    else:
        final = weight,'average'
    return final

def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    is_it_a_leap_year = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_it_a_leap_year = True
    else:
        is_it_a_leap_year = False
    return is_it_a_leap_year

def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    hurricane = ""
    
       
    if(speed > 0and speed<39):
        hurricane+= "Breeze"
    elif(speed>=39 and speed<= 61):
        hurricane+= "Strong Wind"
    elif(speed>=62 and speed<=88):
        hurricane+= "Gale Winds"
    elif(speed>=89 and speed<=117):
        hurricane+= "Whole Gale"
    elif(speed>117):
        hurricane+= "Hurricane"
    else:
        hurricane+= "Unknown"
    return hurricane

def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    location = ""
    if(x > 0 and y > 0):
        location+= "Quadrant 1"
    elif((x == 0) and (y > 0 or y < 0)):
         location+= "Y-Axis"
    elif((y == 0) and (x > 0 or x < 0)):
         location+= "X-Axis"
    elif(x < 0 and y > 0):
        location+= "Quadrant 2"
    elif(x < 0 and y < 0):
        location+= "Quadrant 3"
    elif(x > 0 and y < 0):
        location+= "Quadrant 4"
    else:
        location+= "Origin"
        
    return location

def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    AGE = int(input("enter your age"))
    PRICE = 0
    
    if(AGE < 3):
        price = 0
    elif(AGE>=3 and AGE < 10):
        PRICE = 2.00
    elif(AGE >=10 and AGE < 18):
        student_of_school = input("are you from this school")
        if(student_of_school =="Y"):
            PRICE = 1.00
        else:
            PRICE = 3.00
    elif(AGE>= 18 and AGE <65):
        PRICE = 5.00
    else:
        PRICE = 4.00
    return PRICE
          
        
    
        