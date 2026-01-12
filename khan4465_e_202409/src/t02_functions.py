"""
-------------------------------------------------------
Exam Task 2 Function Definitions: while loop
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-12-05"
-------------------------------------------------------
"""
# Constants

# your constants here


def categorize_temperatures():
    """
    -------------------------------------------------------
    Asks the user for daily temperatures.
    The function stops when the user enters -99.
    The function returns:
        the total number of cold days (temperature <= 0°C)
        the total number of mild days (temperature 1°C - 20°C)
        the total number of hot days (temperature > 20°C)
        the average temperature of all days (rounded down)
    Do all inputs and calculations in integer.
    Use: cold_days, mild_days, hot_days, avg_temp = categorize_temperatures()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        cold_days - number of cold days (int)
        mild_days - number of mild days (int)
        hot_days - number of hot days (int)
        avg_temp - average temperature of all days (int)
    -------------------------------------------------------
    """

    # your code here
    user = int(input("Temperature (-99 to stop): "))
    
    COLD_DAYS= 0
    MILD_DAYS = 0
    HOT_DAYS = 0
    AVG_TEMP = 0
    user_input = 0
    total = 0
    while(user != -99):
        if(user <= 0):
            COLD_DAYS+=1
        if(user >= 0 and user <=20):
            MILD_DAYS+=1
        if(user > 20):
            HOT_DAYS+=1
        user_input+=1
        total+= user
        user = int(input("Temperature (-99 to stop): "))


    return COLD_DAYS,MILD_DAYS,HOT_DAYS,total/user_input
