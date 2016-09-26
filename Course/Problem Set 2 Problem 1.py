balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

currentMonth = 1
while currentMonth < 13:
    monthminpay = balance * monthlyPaymentRate
    monthunpaidbalance = balance - monthminpay
    balance = round(monthunpaidbalance + monthunpaidbalance * (annualInterestRate / 12), 2)
    currentMonth += 1
print(balance)