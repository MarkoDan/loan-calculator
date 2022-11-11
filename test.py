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
    i = loan_interest_percentage / 1200
    
    x = (payment / payment - i * principal)
    base = 1 + i
    print(math.log(base, x))
    
    '''for anyone whos struggling with the log function in example 1:
    n = log 1 + i (A / A − i ∗ P)
    math.log(x, base)
    x = (A / A − i ∗ P)
    base = 1 + i'''