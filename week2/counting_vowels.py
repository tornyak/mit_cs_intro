__author__ = 'vanja'

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5
"""

def countVowels(s):
    cnt = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in s.lower():
        if c in vowels:
            cnt += 1
    return cnt


print("Number of vowels: {0}".format(countVowels("AaeEEE")))
