__author__ = 'etkvadi'

# Lec 2.6, slide 4

x = 6

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')


# Check https://docs.python.org/2/reference/expressions.html#not-in
# string is always bigger than any int
temp = '32'
if temp > 85:
   print "Hot"
elif temp > 62:
   print "Comfortable"
else:
   print "Cold"


varA = 4
varB = 6

if type(varA) is str or type(varB) is str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")


