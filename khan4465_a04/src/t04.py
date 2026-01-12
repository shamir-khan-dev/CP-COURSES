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

from Queue_array import Queue

s1 = Queue()
s2 = Queue()
s3 = Queue()
for x in range(5):
    s1.insert(x)

for x in range(6,9):
    s2.insert(x)

print(s1)
print(s2)
print(s3.combine(s1,s2))
