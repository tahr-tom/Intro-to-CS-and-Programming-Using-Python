balance = 42
annual_interest_rate = 0.2
monthly_payment_rate = 0.04

currentMonth = 1
while currentMonth < 13:
    month_min_payment = balance * monthly_payment_rate
    monthly_unpaid_balance = balance - month_min_payment
    balance = round(monthly_unpaid_balance + monthly_unpaid_balance * (annual_interest_rate / 12), 2)
    currentMonth += 1
print(balance)
