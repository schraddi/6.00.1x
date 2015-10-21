"""

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Test Case 1:
	      balance = 4213
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04 """
	      
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
paid = 0

def format(inputFloat):
    return str(round(inputFloat,2))

for month in range(1,13):
    monthlyPayment = monthlyPaymentRate * balance
    paid += monthlyPayment
    monthlyUnpaidBalance = balance - monthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    print "Month: " + str(month)
    print "Minimum monthly payment: " + format(monthlyPayment)
    print "Remaining balance: " + format(balance)

print "Total paid: " + format(paid)
print "Remaining balance: " + format(balance)