__author__ = 'vanja'

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    result = 1
    # Your Code Here
    while (b ** result) <= x:
        result += 1

    return result-1


#print myLog(16, 2)
#print myLog(15, 3)

def lessThan4(aList):
    '''
    aList: a list of strings
    '''

    return [w for w in aList if len(w) < 4]

#print lessThan4(["apple", "cat", "dog", "banana"])

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N == 0:
        return 0
    else:
        return (N%10) + sumDigits(N/10)


#print sumDigits(0)
#print sumDigits(1)
#print sumDigits(123456789)

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    return sorted([k for k in aDict.keys() if aDict[k] == target ])


#print keysWithValue({6:4, 5:7, 3:7, 1:123, 12:9, 9887:7, 11:6, 4:7}, 7)



def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here

    idx = 0
    while len(L) > 0 and idx < len(L):
        w = L[idx]
        if not f(w):
            L.remove(w)
        else:
            idx += 1

    return len(L)

def f(s):
    print "'a' in ", s, " is ", 'a' in s
    return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L


L = []
print satisfiesF(L)
print L


L = ['']
print satisfiesF(L)
print L

L = ['aheljaej', 'aaaajkdjkaj', 'xxxsdd', 'dgggre4rrg']
print satisfiesF(L)
print L