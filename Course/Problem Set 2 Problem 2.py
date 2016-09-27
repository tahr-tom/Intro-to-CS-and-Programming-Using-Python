def get_balance_after12month(a, b, c):
    """
    Calculate the balance of a credit card with fixed monthly c for 1 year
    :param a: int, balance of a credit card
    :param b: float
    :param c: int, multiples of 10
    :return:
    """
    current_month = 1
    while current_month < 13:
        monthly_unpaid = a - c
        a = monthly_unpaid + monthly_unpaid * (b / 12)
        current_month += 1
    return a

balance = 3926
annual_interest_rate = 0.2
lowest_payment = 300
guess = get_balance_after12month(balance, annual_interest_rate, lowest_payment)
while guess >= 0:
    lowest_payment += 10
    guess = get_balance_after12month(balance, annual_interest_rate, lowest_payment)
print('Lowest Payment:', lowest_payment)
