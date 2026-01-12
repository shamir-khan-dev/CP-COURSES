"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports

# Constants

from List_array import List
from Queue_array import Queue

s1 = List()

s1.append(1)
s1.append(2)
s1.append(3)
s1.append(4)
s1.append(4)
s1.append(4)


s1.insert(-1, 0)

print(s1)
print(s1.remove(1))

print(s1.index(2))

print(s1.find(2))

print(s1.count(4))

print("this is the max value: ", s1.max())
print("this is the min value: ", s1.min())

print(s1.__setitem__(1,10))

print(s1)



