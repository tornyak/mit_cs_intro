__author__ = 'vanja'

"""
    Write a generator, genPrimes, that returns the sequence of prime
    numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
    Have the generator keep a list of the primes it's generated.
    A candidate number x is prime if (x % p) != 0 for all earlier primes p.
"""

def genPrimes():
    primes = []
    last = 1

    def isPrime():
        for p in primes:
            if (last % p) == 0:
                return False
        return True

    while True:
        found = False
        while not found:
            last += 1
            if isPrime():
                yield last
                found = True
                primes.append(last)





primes = genPrimes()

for i in range(0,100):
    print primes.next()
