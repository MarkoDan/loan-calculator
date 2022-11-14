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
    loan_interest = float(input())
    i = loan_interest / 1200
    total_months = math.ceil(math.log(float(monthly_payment) / (float(monthly_payment) - i * float(principal)), i + 1))
    years = total_months // 12

    months = total_months % 12

    print(f"It will take {years} years and {months} months to repay this loan!")

elif calculation == 'a':
    print("Enter the loan principal")
    principal = float(input())
    print("Enter the number of periods")
    periods = int(input())
    print("Enter the loan interest")
    interest = float(input())

    # annual interest rate
    r = (interest / 100) / 12

    g = 1 + r
    x = principal * r
    y = math.pow(g, periods)
    m = math.ceil((x * y) / (y - 1))
    print(f"Your monthly payment = {m}!")

elif calculation == 'p':
    print("Enter the annuity payment:")
    a = float(input())
    print("Enter the number of periods")
    periods = int(input())
    print("Enter the loan interest:")
    interest = float(input())

    i = (interest / 100) / 12

    x = i * math.pow(i + 1, periods)
    y = math.pow(1 + i, periods) - 1
    z = x / y

    p = int(a / z)
    print(f"Your loan principal = {p}!")


