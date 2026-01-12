"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-02"
-------------------------------------------------------
"""
# Imports

# Constants

from Queue_circular import Queue

s1 = Queue()
s2 = Queue()


for x in range(5):
    s1.insert(x)
for u in range(5):
    s2.insert(u)

print(s1)
print(s2)


s1.remove()
s2.remove()

print(s1)
print(s1.__eq__(s2))

