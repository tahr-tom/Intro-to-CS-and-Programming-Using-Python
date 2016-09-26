# Guess a number between 0(inclusive) and 100(exclusive)
lower = 0
upper = 100
guess = int((lower + upper) / 2)
print('Please think of a number between 0 and 100!')
print('Is your secret number', guess, '?')
choice = input("Enter 'h' to indicate the guess is too high. "
               "Enter 'l' to indicate the guess is too low. "
               "Enter 'c' to indicate I guessed correctly.")
while choice != 'c':
    if choice == 'h':
        upper = guess
        guess = int((lower + upper) / 2)
        print('Is your secret number', guess, '?')
        choice = input("Enter 'h' to indicate the guess is too high. "
                       "Enter 'l' to indicate the guess is too low. "
                       "Enter 'c' to indicate I guessed correctly.")
    elif choice == 'l':
        lower = guess
        guess = int((lower + upper) / 2)
        print('Is your secret number', guess, '?')
        choice = input("Enter 'h' to indicate the guess is too high. "
                       "Enter 'l' to indicate the guess is too low. "
                       "Enter 'c' to indicate I guessed correctly.")
    elif choice == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number', guess, '?')
        choice = input("Enter 'h' to indicate the guess is too high. "
                       "Enter 'l' to indicate the guess is too low. "
                       "Enter 'c' to indicate I guessed correctly.")
print('Game over. Your secret number was:', guess)
