# MITx 6.00.1
# Problem Set 2 / Problem 3
# USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER (Credit Card)

#initializing
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
hi = (balance * (1 + monthlyInterestRate)**12)/12.0
lo = balance/12
newBalance = (hi + lo)/2
update = True

def monthlyPayment(balance,monthlyInterestRate,newBalance):
    '''
    balance - the outstanding balance
    monthlyInterestRate -  monthly interest rate
    '''
    month = 1
    while month < 13:
        balance -=  newBalance 
        balance += monthlyInterestRate*balance 
        month += 1
    return balance

while update:
    pay = monthlyPayment(balance,monthlyInterestRate,newBalance)
    if  round(pay) < 0:
        hi = newBalance
        newBalance = (hi + lo)/2
    elif round(pay) > 0:
        lo = newBalance
        newBalance = (hi + lo)/2
    elif round(pay) == 0:
        update = False
        print 'Lowest Payment:',round(newBalance, 2)