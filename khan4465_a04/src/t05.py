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

from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()

for x in range(5):
    source.insert(x)
    
source.insert(2)
source.insert(2)

print(source)

print(pq_split_key(source,2))