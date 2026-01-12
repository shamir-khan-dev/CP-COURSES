"""
-------------------------------------------------------
Testing for Task 2: while loop
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      987654321
Email:   ssehra@wlu.ca
__updated__ = "2024-12-01"
-------------------------------------------------------
"""
from t02_functions import categorize_temperatures
cold_days, mild_days, hot_days, avg_temp = categorize_temperatures()
# enter 
#  Temperature (-99 to stop): -5
#  Temperature (-99 to stop): 10
#  Temperature (-99 to stop): 25
#  Temperature (-99 to stop): -10
#  Temperature (-99 to stop): -99
print(f"Cold days: {cold_days}, Mild days: {mild_days}, Hot days: {hot_days}, Average temperature: {avg_temp}")
