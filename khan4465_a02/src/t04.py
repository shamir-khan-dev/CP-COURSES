"""
-------------------------------------------------------
[Assignment 2, Task 4]
Calculating annual task on sales
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-29"
-------------------------------------------------------
"""
# Imports

number_of_flyers = int(input("Number of flyers: "))
number_of_delivery_people = int(input("Number of delivery people: ")) 

flyers_per_delivery_person = number_of_flyers // number_of_delivery_people
flyers_left_over = number_of_flyers % number_of_delivery_people

print(f'''Flyers per delivery person: {flyers_per_delivery_person}
Flyers left over: {flyers_left_over}''')
