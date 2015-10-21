# -*- coding: utf-8 -*-
# Vorgaben
balance = 3192
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate) / 12.0
startBalance = balance

monthlyPayment = 0.0

while balance > 0:
    balance = startBalance
    monthlyPayment += 0.01
    for month in range(1, 13):
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

print "Lowest Payment: " + str(monthlyPayment)
