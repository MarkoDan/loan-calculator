import math
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--type', metavar='type', type=str, help='enter the type of calculator')
    parser.add_argument('--principal', type=int)
    parser.add_argument('--payment', type=int)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--periods', type=int)
    args = parser.parse_args()

    calculator_type = args.type
    principal = args.principal
    payment = args.payment
    interest = args.interest
    periods = args.periods


    if calculator_type == 'diff' and args.principal and args.periods and args.interest:
        diff_payment_calculator(principal, interest, periods)
    elif calculator_type == 'annuity' and args.principal and args.periods and args.interest:
        annuity_payment_calculator(principal, periods, interest)
    elif calculator_type == 'annuity' and args.payment and args.periods and args.interest:
        annuity_principal_calculator(payment, periods, interest)
    elif calculator_type == 'annuity' and args.principal and args.payment and args.interest:
        annuity_period_calculator(principal, payment, interest)
    else:
        print('Incorrect parameters')



def diff_payment_calculator(principal, interest, periods):
    i = interest / 1200
    x = principal / periods
    all_payments = 0
    m = 1
    while m <= periods:
        y = principal - (principal * (m - 1) / periods)
        result = math.ceil(x + i * y)
        print(f"Month {m}: payment is {result}")
        all_payments += result
        m += 1
    overpayment = all_payments - principal
    print()
    print(f"Overpayment = {overpayment}")

def annuity_payment_calculator(principal, periods, interest):
    i = interest / 1200
    x = principal * i
    y = math.pow(1 + i, periods)
    m = math.ceil((x * y) / (y - 1))
    overpayment = m * periods - principal
    print(f"Your annuity payment = {m}!")
    print(f'Overpayment = {overpayment}')


def annuity_principal_calculator(payment, periods, interest):
    i = interest / 1200
    x = i * math.pow(i + 1, periods)
    y = math.pow(1 + i, periods) - 1
    z = x / y
    p = int(payment / z)
    overpayment = (payment * periods) - p
    print(f"Your loan principal = {p}!")
    print(f"Overpayment = {overpayment}")

def annuity_period_calculator(principal, payment, interest):
    i = interest / 1200
    total_months = math.ceil(math.log(float(payment) / (float(payment) - i * float(principal)), i + 1))
    years = total_months // 12
    months = total_months % 12
    if months == 0 and years > 1:
        print(f'It will take {years} years to repay this loan!')
    elif months == 0 and years == 1:
        print(f'It will take {years} year to repay this loan!')
    elif months > 1 and years > 1:
        print(f"It will take {years} years and {months} months to repay this loan!")

    overpayment = total_months * payment - principal
    print(f'Overpayment = {overpayment}')


if __name__ == '__main__':
    main()

