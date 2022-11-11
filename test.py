import math

print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
calculation = input()

if calculation == 'n':
    print('Enter the loan principal:')
    principal = int(input())
    print('Enter the monthly payment:')
    payment = int(input())
    print('Enter the loan interest:')
    loan_interest_percentage = int(input())
    interest = principal / loan_interest_percentage
    p = 12 * principal
    i = interest / p
    x = principal * i
    pv = x / payment
    result = 1 - pv

    n = math.log(result) / math.log(i)

    print(n)

elif calculation == 'a':
    print('Enter the loan principal:')
    principal = int(input())
    print('Enter the number of periods:')
    periods = int(input())
    print('Enter the loan interest:')
