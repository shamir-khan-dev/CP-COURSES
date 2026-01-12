"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-29"
-------------------------------------------------------
"""
# Imports

foundation_length = float(input("enter foundation length: "))
foundation_width = float(input("enter foundation width: "))
foundation_height = float(input("enter foundation height: "))
wall_height = float(input("enter wall height: "))
cost_of_concrete = float(input("Cost of concrete ($/m^3): "))
cost_of_bricks = float(input("Cost of concrete ($/m^3): "))


concrete_needed_for_foundation = (foundation_length * foundation_width * foundation_height)

total_cost_of_concrete = concrete_needed_for_foundation * cost_of_concrete

bricks_needed_for_walls = (((wall_height * foundation_length) * 2) + ((wall_height * foundation_width) *2))

total_cost_of_bricks = bricks_needed_for_walls * cost_of_bricks

total = total_cost_of_bricks + total_cost_of_concrete


print(f'''Concrete needed for foundation (m^3): {concrete_needed_for_foundation}
Cost of concrete: ${total_cost_of_concrete:,.2f}
Bricks needed for walls (m^2): {bricks_needed_for_walls} ''')
print(f"Cost of bricks: ${total_cost_of_bricks:,.2f}")
print(f"Total cost: ${total:,.2f}")