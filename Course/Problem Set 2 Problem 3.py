balance = 999999
annual_interest_rate = 0.18

init_balance = balance
monthly_interest_rate = annual_interest_rate / 12.0
lower = balance / 12
upper = (balance * (1 + monthly_interest_rate) ** 12) / 12.0

while balance != 0.00:
    guess = (lower + upper) / 2
    balance = init_balance
    for i in range(1, 13):
        balance = (balance - guess) * (1 + monthly_interest_rate)
    if balance > 0:
        lower = guess
    elif balance < 0:
        upper = guess
    balance = round(balance, 2)
guess = round(guess, 2)
print('Lowest Payment:', guess)
