"""
-------------------------------------------------------
Midterm Task 5 Testing
-------------------------------------------------------
Author:  Sukhjit Singh Sehra
ID:      11111111
Email:   ssehra@wlu.ca
__updated__ = "2024-10-22"
-------------------------------------------------------
"""
# Imports

from t05_functions import order_status

feedback = input("Enter Feedback: ")
status = order_status(feedback)
print(f"result('{feedback}') -> Status: {status}")
