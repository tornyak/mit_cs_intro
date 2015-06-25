__author__ = 'vanja'

"""
# The program works as follows: you (the user) thinks of an integer
# between 0 (inclusive) and 100 (not inclusive). The computer makes guesses,
# and you give it input - is its guess too high or too low? Using bisection
# search, the computer will guess the user's secret number!

Example:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83


"""

inputMsg = "Enter 'h' to indicate the guess is too high.\
 Enter 'l' to indicate the guess is too low.\
 Enter 'c' to indicate I guessed correctly. "

print("Please think of a number between 0 and 100!")

low = 0
high = 100

while True:
    guess = (high + low) / 2
    print "Is your secret number {0}?".format(guess)
    mInput = mInput = raw_input(inputMsg)
    while mInput not in ['c','h','l']:
        print("Sorry, I did not understand your input.")
        print("Is your secret number {0}?".format(guess))
        mInput = raw_input(inputMsg)
    if mInput == 'c':
        print("Game over. Your secret number was: {0}".format(guess))
        break
    elif mInput == 'l':
        low = guess
    else:
        high = guess


