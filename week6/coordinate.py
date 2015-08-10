__author__ = 'vanja'

import math

def sq(x):
    return x*x


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

    def distance(self,other):
        return math.sqrt(sq(self.x - other.x)
                         + sq(self.y - other.y))

    def __eq__(self, other):
        if other != None and isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return 'Coordinate({0}, {1})'.format(self.x, self.y)

c = Coordinate(3,4)
Origin = Coordinate(0,0)

print c
print Origin
print c.distance(Origin)
print type(c)
print isinstance(c, Coordinate)

a = Coordinate(1,2)
b = Coordinate(1,2)

print a == b
print a == c
print a == None
print repr(a)



