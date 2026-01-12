"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports

cost_of_food = input("Price of the food: ")

cost = float(cost_of_food)

tax_percent = input("How much was the tax percent: ")

tax = float(tax_percent)

tax_percentage = tax/100

tip_percent = input("How much was the tip percent: ")

tip = float(tip_percent)

tip_percentage = tip/100

total = ((tax/100)*cost) + ((tip/100)*cost) + cost
if(tax_percentage < 10):
    tax_percentage = tax_percentage * 10
if(tip_percentage< 10):
    tip_percentage = tip_percentage * 10
    
print(f"""Subtotal: $ {cost_of_food}
     Tax: $ {tax_percentage}
     Tip: $ {tip_percentage}
------------------
   Total: $ {total}""")