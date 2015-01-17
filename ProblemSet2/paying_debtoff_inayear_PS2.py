# MITx 6.00.1
# Problem Set 2 / Problem 2
# PAYING DEBT OFF IN A YEAR (Credit Card)

#initialize variables/info
balance = 3329
annualInterestRate = 0.2
newBalance = 0
update = True

# function that holds the balance and annualInterestRate
# used to calculate the minimum fixed monthly payment 
# needed in order pay off a credit card balance within 12 months
def monthlyPayment(balance,annualInterestRate,newBalance):
    '''
    balance - the outstanding balance
    annualInterestRate - annual interest rate
    '''
    month = 1
    while month <= 12:
        balance -=  newBalance 
        balance += (annualInterestRate/12.0)*balance 
        month += 1
    if balance <= 0:
        return newBalance
    else:
        return False

while update == True:
    if monthlyPayment(balance,annualInterestRate,newBalance):
        update = False
        print 'Lowest Payment:',monthlyPayment(balance,annualInterestRate,newBalance)
    else:
        newBalance += 10
        monthlyPayment(balance,annualInterestRate,newBalance)