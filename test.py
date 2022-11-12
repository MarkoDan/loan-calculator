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
    monthly_payment = int(input())
    print('Enter the loan interest:')
    loan_interest = int(input())
    i = loan_interest / 1200

    months = round(math.log(float(monthly_payment) / (float(monthly_payment) - i * float(principal)), i + 1))
    
    years = months / 12

    print(years)
    
   