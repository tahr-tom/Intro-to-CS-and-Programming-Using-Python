# Generate a number between lower limit(inclusive) and upper limit(inclusive)
# Ask user to input a number inside the range
# If the number is wrong, narrow down the range
import random
lower = int(input('Please enter the lower limit(inclusive): '))
upper = int(input('Please enter the upper limit(inclusive): '))
answer = random.randint(lower - 1, upper + 1)
print('The answer is', answer)  # For debug only
guess = int(input('Please enter the your guess: '))
tries = 0
while guess != answer:
    if guess > upper or guess < lower:
        print('Error! You have enter a number which is not inside the range')
        guess = int(input('Please enter the your guess: '))
    elif guess > answer:
        tries += 1
        upper = guess
        print('The answer is between', lower, 'and', upper)
        guess = int(input('Please enter the your guess: '))
    elif guess < answer:
        tries += 1
        lower = guess
        print('The answer is between', lower, 'and', upper)
        guess = int(input('Please enter the your guess: '))
tries += 1
print('Congratulations! You get the answer in', tries, 'tries')
