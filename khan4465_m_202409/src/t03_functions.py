"""
-------------------------------------------------------
Midterm AB Task 3 Function Definition
-------------------------------------------------------
Author: Shamir Khan
ID:     169094465
Email:  khan4465@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""
# Constants

# your constants here


def gym_membership_cost():
    """
    -------------------------------------------------------
    Determines the cost of a gym membership. The cost is made up of:
        base membership cost: $50.00
        cost per additional class: $20.00
        loyalty discount 10% only if more than 2 additional classes are purchased and 
        the member has been with the gym for more than 1 year.
    The function must ask the user for these inputs.
    Use: cost = gym_membership_cost()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​‌​​​​‌​‌‌​‌​‌​​​​​‌:
        cost - total cost of the gym membership based upon the base cost, the number of 
        additional classes purchased, and loyalty discount if applicable (float)
    -------------------------------------------------------
    """

    # your code here

    cost_per_additional_class = int(input("How many additional classes are you purchasing? "))
    
    total = 0 
    if(cost_per_additional_class<=2):
        total += 50 + (20*cost_per_additional_class)
    elif(cost_per_additional_class > 2 ):
        loyalty = int(input("How many years have you been a member? "))
        if(loyalty>1):
            total += 50 + (20*cost_per_additional_class) - ((50 + (20*cost_per_additional_class)) * (10/100))
        else:
             total += 50 + (20*cost_per_additional_class)
    else:
        total += 50 + (20*cost_per_additional_class)
    total = float(total)
        
    return total
