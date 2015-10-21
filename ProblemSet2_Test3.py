# -*- coding: utf-8 -*-
# Vorgaben
balance = 17000
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate) / 12.0
startBalance = balance
monthlyPaymentLowerBound = balance / 12.0
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12

monthlyPayment = 0.0

while balance > 0 or balance < -0.01:
    balance = startBalance
    monthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2.0
    for month in range(1, 13):
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    if balance > 0:
        monthlyPaymentLowerBound = monthlyPayment
    else:
        monthlyPaymentUpperBound = monthlyPayment
        

print "Lowest Payment: " + str(round(monthlyPayment,2))
