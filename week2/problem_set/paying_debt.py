__author__ = 'vanja'

"""
    Now write a program that calculates the minimum fixed monthly payment
    needed in order pay off a credit card balance within 12 months. By a
    fixed monthly payment, we mean a single number which does not change
    each month, but instead is a constant amount that will be paid each month.
    In this problem, we will not be dealing with a minimum monthly payment rate.

    The following variables contain values as described below:

        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal

    The program should print out one line: the lowest monthly payment that will
    pay off all debt in under 1 year, for example:

        Lowest Payment: 180

    Assume that the interest is compounded monthly according to the balance at the
    end of the month (after the payment for that month is made). The monthly payment
    must be a multiple of $10 and is the same for all months. Notice that it is
    possible for the balance to become negative using this payment scheme, which is okay.
    A summary of the required math is found below:

        Monthly interest rate = (Annual interest rate) / 12.0
        Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
        Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 4773
annualInterestRate = 0.2


def isEnough(balance, annualInterestRate, minPayment):
    for month in range(1,13):
        interest = ((annualInterestRate/12) * (balance - minPayment))
        balance -= (minPayment - interest)
        if balance <= 0:
            return True

    return False



def brute(balance, annualInterestRate):
    minPayment = 10
    while not isEnough(balance, annualInterestRate, minPayment):
        minPayment += 10

    print("Lowest Payment: {}".format(minPayment))


def bisection(balance, annualInterestRate):
    # convert to cents
    lowerBound = balance / 12
    upperBound = balance * (1 + annualInterestRate) / 12
    epsilon = 0.01
    minPayment = (lowerBound + upperBound) / 2

    while (upperBound - lowerBound) > epsilon:
        if isEnough(balance, annualInterestRate, minPayment):
            upperBound = minPayment
            minPayment = (lowerBound + upperBound) / 2
        else:
            lowerBound = minPayment
            minPayment = (lowerBound + upperBound) / 2

    print("Lowest Payment: {:.2f}".format(minPayment))


brute(balance, annualInterestRate)
bisection(320000, 0.2)