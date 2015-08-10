# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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

    for letter in secretWord:
        if not (letter in lettersGuessed):
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = []
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed.append(letter)
        else:
            guessed.append('_ ')

    return ''.join(guessed)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    remaining = []

    for letter in string.ascii_lowercase:
        if not (letter in lettersGuessed):
            remaining.append(letter)
    return ''.join(remaining)

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

    print('Welcome to the game, Hangman!')
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    print('-------------')

    guessesLeft = 8
    lettersGuessed = []
    avaliableLetters = getAvailableLetters(lettersGuessed)
    guessedWord = getGuessedWord(secretWord, lettersGuessed)

    while guessesLeft > 0:
        print("You have {} guesses left.".format(guessesLeft))
        print("Available letters: {}".format(avaliableLetters))
        letter = raw_input("Please guess a letter: ").lower()

        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(guessedWord))
            print('-------------')
            continue

        lettersGuessed.append(letter)
        avaliableLetters = getAvailableLetters(lettersGuessed)
        if letter in secretWord:
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print("Good guess: {}".format(guessedWord))
            print('-------------')
            # check for win
            if isWordGuessed(secretWord, lettersGuessed):
                print("Congratulations, you won!")
                return None
        else:
            guessesLeft -= 1
            print("Oops! That letter is not in my word: {}".format(guessedWord))
            print('-------------')

    print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
