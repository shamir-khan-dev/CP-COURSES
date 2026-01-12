"""
-------------------------------------------------------
sorting number of flyers for volunteers
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports

number_of_flyers = int(input("Type the total numbers of flyers: "))

Number_of_volunteers = int(input("Type the total numbers of volunteers: "))

number_of_flyers_per_volunteer = number_of_flyers // Number_of_volunteers

left_over = number_of_flyers % Number_of_volunteers

print(f"Flyers per volunteer: {number_of_flyers_per_volunteer}")
print(f"Flyers left over: {left_over}")
