"""
-------------------------------------------------------
calculating monthly mortgage
-------------------------------------------------------
Author:  shamir khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports

mortgage_principal_amount = float(input("Please enter Mortgage principal amount: ")) 

mortgage_time = int(input("How long will the mortgage last: "))

yearly_interest_rate = int(input("whats the yearly interest rate: "))


interest_rate = (yearly_interest_rate/100)/12

interest_rate_real = float(interest_rate)

monthly_mortgage = (mortgage_time * 12)

mortgage_payment = (mortgage_principal_amount * interest_rate * (1 + interest_rate)**monthly_mortgage) / ((1 + interest_rate)**monthly_mortgage - 1)

mortgage = float(mortgage_payment)

print(f"The monthly payments are: $ {mortgage}")