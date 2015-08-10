__author__ = 'vanja'

"""
    Write a program to calculate the credit card balance after one year if
    a person only pays the minimum monthly payment required by the credit
    card company each month. The following variables contain values as
    described below:

        balance - the outstanding balance on the credit card

        annualInterestRate - annual interest rate as a decimal

        monthlyPaymentRate - minimum monthly payment rate as a decimal

        Month: 1
        Minimum monthly payment: 96.0
        Remaining balance: 4784.0
        ....
        Total paid: 96.0
        Remaining balance: 4784.0
"""

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

remainingBalance = balance
interest = 0.0
total = 0.0

for month in range(1,13):
    minPayment = monthlyPaymentRate * remainingBalance
    interest = ((annualInterestRate/12) * (remainingBalance - minPayment))
    remainingBalance -= (minPayment - interest)
    total += minPayment
    print("Month: {}".format(month))
    print("Minimum monthly payment: {0:.2f}".format(minPayment))
    print("Remaining balance: {0:.2f}".format(remainingBalance))

print("Total paid: {0:.2f}".format(total))
print("Remaining balance: {0:.2f}".format(remainingBalance))


