# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    n = 0
    while n < len(secretWord):
        if secretWord[n] not in lettersGuessed:
            return False
        else:
            n += 1
    return True




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    u = ' _ '
    n = 0
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans += letter
        else:
            ans += u
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    abc = string.ascii_lowercase
    string_list = []
    for letter in abc:
        string_list.append(letter)
    for letter in lettersGuessed:
        if letter not in string_list:
            break
        string_list.remove(letter)
    return ''.join(string_list)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    length = len(secretWord)

    # Some format
    right = 'Good guess: '  # sentence for right guess
    wrong = "Oops! That letter is not in my word:"  # sentence for wrong guess
    same = "Oops! You've already guessed that letter:"  # sentence for same guess
    available = 'Available letters:'  # sentence for available or not
    win = 'Congratulations, you won!'  # sentence for win
    lose = 'Sorry, you ran out of guesses.'  # sentence for lose
    ans_reveal = 'The word was'
    format_line = '------------'
    chance = 8  # remain guesses
    letterGuessed = []

    print('Welcome to the game, Hangman!')
    print('I am thinking a word that is', length, 'long.')
    print(format_line)
    while chance != 0:
        print('You have', chance, 'guesses left.')
        print(available, getAvailableLetters(letterGuessed))
        guess = input('Please guess a letter: ')
        guesslower = guess.lower()
        if guesslower in letterGuessed:
            print(same, getGuessedWord(secretWord, letterGuessed))
            print(format_line)
        else:
            letterGuessed += guesslower
            if guesslower in secretWord:
                print(right, getGuessedWord(secretWord, letterGuessed))
                print(format_line)
            else:
                print(wrong, getGuessedWord(secretWord, letterGuessed))
                print(format_line)
                chance -= 1
        if isWordGuessed(secretWord, letterGuessed):
            print(win)
            break
    if not(isWordGuessed(secretWord, letterGuessed)):
        print(lose, ans_reveal, secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
hangman('sea')
