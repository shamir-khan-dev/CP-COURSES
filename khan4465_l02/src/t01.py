"""
-------------------------------------------------------
converting a celsius temperature to fahrenheit
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports

celsius = int(input("Enter the celsius value which you want to convert to fahrenheit: "))

WATER = 32
fahrenheit = (9/5 *celsius) + WATER

print("Temperature (F):",int(fahrenheit))


