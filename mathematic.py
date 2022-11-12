import math

principal = 1000000

monthly_payment = 15000

loan_interest = 10

i = loan_interest / 1200

month = round(math.log(float(monthly_payment) / (float(monthly_payment) - i * float(principal)), i + 1))
print(month)