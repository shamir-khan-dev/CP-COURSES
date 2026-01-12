"""
-------------------------------------------------------
[Lab 7,functions]
function which does various operations
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-11-01"
-------------------------------------------------------
"""
# Imports

from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    
    """
    number = randint(1, high)
    guesses = 1
    guess = int(input("Guess: "))
    
    while(guess!=number):
        if(guess>number):
            print(f"""Too high, try again.""")
            guess = int(input("Guess: "))
            guesses+=1
            
        elif(guess<number):
            print(f"""Too low, try again.""")
            guess = int(input("Guess: "))
            guesses+=1
                
    print(f"""Congratulations - good guess!
You made {guesses} guesses.""")
            
    
    return guesses         
        
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    two_squared = 1
    power = 0
    while(two_squared < target):
        power+=1
        two_squared = 2**power
    return 2**(power)

def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    
    first_value = float(input("First positive value: ")) 
    
    minimum = first_value
    
    maximum = first_value
    
    total = first_value
    
    total_inputs = 1
    
    next_value = first_value
    while(next_value >= 0):
        next_value = float(input("Next positive value: "))
        if(next_value<minimum and next_value>=0 ):
            total_inputs+=1
            total+=next_value
            minimum = next_value
        if(next_value>maximum and next_value>=0):
            total_inputs+=1
            total+=next_value
            maximum = next_value
    return float(minimum),float(maximum),float(total),float(total/total_inputs)

def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    user_input = float(input("Enter an expense (0 to quit): $"))
    total_expenses = user_input
    status = ""
    while(user_input != 0):
        user_input = float(input("Enter another expense (0 to quit): $"))
        total_expenses+=user_input
    total = float(available - total_expenses)
    if(total < available):
        status = "Deficit"
    elif(total > available):
        status = "Surplus"
    else:
        status = "Balanced"
    
    return total_expenses,total,status
        
        
from random import randint

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    
    employee = int(input("Employee ID: "))
    total = 0
    count = 0
    TAXRATE = (1 - 3.625 / 100)
    OVERTIME = 1.5
    while(employee != 0):
        count += 1
        hourly_wage_rate = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))

        if(hours_worked > 40):
            OVERTIMEHOURS = hours_worked - 40
            gross_pay = (40 * hourly_wage_rate) + (OVERTIMEHOURS * hourly_wage_rate * OVERTIME)
        else:
            gross_pay = hourly_wage_rate * hours_worked

        
        net_pay = gross_pay * TAXRATE
        total += net_pay

        print(f"Net payment for employee {employee}: ${net_pay:.2f}")
        
        employee = int(input("Employee ID: "))
    
    
    return round(float(total),2),round(float(total/count),2)
    