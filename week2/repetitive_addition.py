__author__ = 'vanja'

# lecture 3.1, slide 2

# repetitive addition

x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft -1
print(str(x) + '*' + str(x) + ' = ' +str(ans))


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)

for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!'

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)



