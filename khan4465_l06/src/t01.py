"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-03-03"
-------------------------------------------------------
"""
# Imports

# Constants

from List_linked import List


list_one = List()
list_two = List()
list_three = List()
list_four = List()
list_five = List()
list_six = List()




for x in range(10):
    list_one.append(x)

for x in range(10):
    list_two.append(x)


print(list_one)
print(list_two)



list_four.intersection(list_one, list_two)

print(list_four, "List 4")

list_five.append(1)

print(list_five)

print(list_five.remove_many(1))

print(list_five)
