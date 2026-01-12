"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-09"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants

s1 = List()
s2 = List()
s3 = List()
s4 = List()
s5 = List()
for x in range(5):
    s1.append(x)
    s2.append(x)
print(s1)
print(s2)
print(s1.__eq__(s2)) # or better way just do this, look at the line below
print(s1 == s2)


print(s1.__getitem__(1))# or better way just do this, look at the line below
print(s1[1])
    
for x in range(5):
    s1.append(5)
    s1.append(2)

print(s1)
print(s1.clean())
print("this is:",s1)

print(s1,s2)

print(s3.combine(s1, s2))
print(s3)

for x in range(5):
    s1.append(x)
    s2.append(x)

s2.append(6)

print(s4.intersection(s1,s2))

print("This is s4:" , s4)

s4.prepend(10)
print("new s4: ", s4)

print(s4.remove_front())

print(s4)

print(s4.remove_many(6))
s4.append(7)
s4.append(7)

print("this",s4)
print("yea", s4.split_alt())


a = [1,2,3,4]
b = [1,2,3,4,5]

s5.union(a, b)

print(s5)


#print(s4.split())


