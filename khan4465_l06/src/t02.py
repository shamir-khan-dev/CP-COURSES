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

l1 = List()

l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)

"""
l1.append(5)
l1.append(5)
l1.append(5)
l1.append(1000)
l1.append(0)
"""
print(l1)
print(l1._linear_search(4))
print("it appears ", l1.count(5), " Times")
print(f"This is the biggest number: {l1.max()}")
print(f"This is the smallest number: {l1.min()}")
print(f"This is the result: {l1.find(0)}")
print(f"it found it at index {l1.index(3)}")
print(f"yes it contains {l1.__contains__(5)}")
print(l1)

print(f"It removed {l1.remove(3)}")

print(f"It removed {l1.remove(1)}")
print(f"It removed {l1.remove(9)}")


print(f"the new list {l1}")


l2 = List()

print(f"the new list {l2}")
print(f"the new value appended {l2.append(1)}")
print(f"the new list {l2}")
print(f"It removed {l2.remove(1)}")
print(f"the new list {l2}")

print(f"It removed {l2.remove(1)}")


#rint(l1._linear_search_r(5))
