# MITx 6.00.1
# Problem Set 2 / Problem 1
# PAYING THE MINIMUM (Credit Card)

balance = 4213.00
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 0
totalPaid = 0

for month in range(1,13):
    print "Month: ", month
    
    minMonthlyPayment =  balance * monthlyPaymentRate
    print 'Minimum monthly payment', ('%.2f' % minMonthlyPayment)
    
    balance1 = balance - minMonthlyPayment
    ans1 =  (annualInterestRate/12.0) * balance1
    prevPay = minMonthlyPayment - ans1    
    remBalance = balance - prevPay
    print 'Remaining Balance', ('%.2f' % remBalance)
    
    balance = remBalance
    totalPaid = totalPaid + minMonthlyPayment
    
print 'Total paid: ', ('%.2f' % totalPaid)
print 'Remaining balance: ', ('%.2f' % remBalance)