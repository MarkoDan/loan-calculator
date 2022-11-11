import math

print('Enter the loan principal:')
principal = int(input())
print('What do you want to calculate?')
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment:')
payments = input()

if payments == 'm':
    print('Enter the monthly payment:')
    monthly_payment = int(input())
    months = principal / monthly_payment
    if months == 1:
        print(f"It will take {round(months)} month to repay the loan")
    else:
        print(f"It will take {round(months)} months to repay the loan")
elif payments == 'p':
    print('Enter the number of months:')
    months = int(input())
    payment = principal / months
    if isinstance(payment, float):
        payment = math.ceil(payment)
        last_payment = principal - (months - 1) * payment
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
    elif isinstance(payment, int):
        print(f"Your monthly payment = {payment}")

