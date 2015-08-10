__author__ = 'etkvadi'

"""
http://stackoverflow.com/questions/7942346/how-does-python-compare-functions
"""
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

print b(a,b)