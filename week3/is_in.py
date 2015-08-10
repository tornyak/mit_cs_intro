__author__ = 'vanja'
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    length = len(aStr)
    # Your code here
    if length == 0:
        return False
    else:
        middle = aStr[length / 2]
        if char > middle:
            return isIn(char, aStr[length/2 + 1:length])
        elif char < middle:
            return  isIn(char, aStr[0:length/2])
        else:
            return True


print isIn('x', sorted("ahhfehfdfnkjfaleiueuahjehlkajrejrelrzzy"))


