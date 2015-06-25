__author__ = 'vanja'

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

def count_bob(s):
    cnt = 0
    i = 0
    while i < len(s):
        if s[i:i+3] == 'bob':
            cnt+=1
            i+=2
        else:
            i+=1
    print "Number of times bob occurs is: ", cnt

count_bob('azcbobobegghakl')
count_bob('lboboboboobobg')