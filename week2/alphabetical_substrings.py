__author__ = 'vanja'

"""
    Assume s is a string of lower case characters.

    Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
    For example, if s = 'azcbobobegghakl', then your program should print:

    Longest substring in alphabetical order is: beggh

    In the case of ties, print the first substring.

    For example, if s = 'abcbcd', then your program should print:

    Longest substring in alphabetical order is: abc
"""


s = 'abcbcd'

maxString = ""

i = 0
while i < len(s):
    tmpStr = s[i]
    j = i + 1
    while j < len(s) and s[j-1] <= s[j]:
        tmpStr += s[j]
        j += 1
    if len(tmpStr) > len(maxString):
        maxString = tmpStr
    i = j


print "Longest substring in alphabetical order is: ", maxString
