"""
-------------------------------------------------------
[Assignment 4,functions]
function which does various operations
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-10-13"
-------------------------------------------------------
"""
# Imports

def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    
    day = ""
    if(day_num == 1):
        day+="Sunday"
    elif(day_num == 2):
        day+="Monday"
    elif(day_num == 3):
        day+="Tuesday"
    elif(day_num == 4):
        day+="Wednesday"
    elif(day_num == 5):
        day+="Thursday"
    elif(day_num == 6):
        day+="Friday"
    elif(day_num == 7):
        day+="Saturday"
    else:
        day+="Error"
    return day

def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    poloution = ""
     
    if(air_quality_index >= 0 and air_quality_index <= 50):
        poloution+= "Good"
    elif(air_quality_index >= 51 and air_quality_index <= 100):
        poloution+= "Moderate"
    elif(air_quality_index >= 101 and air_quality_index <= 150):
        poloution+= "Unhealthy for Sensitive Groups"
    elif(air_quality_index >= 151 and air_quality_index <= 200):
        poloution+= "Unhealthy"
    elif(air_quality_index >= 201 and air_quality_index <= 300):
        poloution+= "Very Unhealthy"
    elif(air_quality_index >= 301):
        poloution+= "Hazardous"
    else:
         poloution+= "Error"
    return poloution

def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    values = [val1, val2, val3]
    
    if values[0] > values[1]:
        largest = values[0]
        second_largest = values[1]
    else:
        largest = values[1]
        second_largest = values[0]

# Check the third number
    if values[2] > largest:
        second_largest = largest
        largest = values[2]
    elif values[2] > second_largest:
        second_largest = values[2]
    return  (largest +  second_largest) / 2

def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    color = ""
    if(rgb_colour1 == "red" and rgb_colour2 == "blue" or (rgb_colour1 == "blue" and rgb_colour2 == "red")):
        color+= "fuchsia"
    elif(rgb_colour1 == "red" and rgb_colour2 == "green" or (rgb_colour1 == "green" and rgb_colour2 == "red")):
        color+= "yellow"
    elif(rgb_colour1 == "green" and rgb_colour2 == "blue" or (rgb_colour1 == "blue" and rgb_colour2 == "green")):
        color+= "aqua"
    elif(rgb_colour1 == "red" and rgb_colour2 == "red"):
        color+= "red"
    elif(rgb_colour1 == "blue" and rgb_colour2 == "blue"):
        color+= "blue"
    elif(rgb_colour1 == "green" and rgb_colour2 == "green"):
        color+= "green"
    else:
        color+="Error"
    return color


def hoo_rah(number):
    """
    Add the function to a PyDev module named functions.py. Test it from .

    hoo_rah takes an integer parameter and returns one of the following strings:

    "Hoo" if number is evenly divisible by 2
    "Rah" if number is evenly divisible by 7
    "Hoo Rah" if number is evenly divisible by both 2 and 7
    "Zip" if number is none of the above
    Provide the function docstring (documentation) following the CP104 style.

    The function does not ask for input and does no printing - that is done by your test program.
        
    """
    word = ""
    if(number%7 == 0 and number%2 == 0):
       word+= "Hoo Rah" 
    elif(number%2 == 0):
       word+= "Hoo" 
    elif(number%7 == 0):
        word+= "Rah" 
   
    else:
        word+= "Zip"
    return word
        
        
    
        
        
                
        
    
        
        
        