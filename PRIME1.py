import math


def potential_primes():
    # Make a generator for 2, 3, 5, & thence all numbers coprime to 30
    s = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for i in s:
        yield i
    s = (1,) + s[3:]
    j = 30
    while True:
        for i in s:
            yield j + i
        j += 30


def range_sieve(lo, hi):
    # Create a list of all primes in the range(lo, hi)
    # Mark all numbers as prime
    primes = [True] * (hi - lo)
    # Eliminate 0 and 1, if necessary
    for i in range(lo, min(2, hi)):
        primes[i - lo] = False
    ihi = int(math.sqrt(hi))
    for i in potential_primes():
        if i > ihi:
            break
        # Find first multiple of i: i >= i*i and i >= lo
        ilo = max(i, 1 + (lo - 1) // i) * i
        # Determine how many multiples of i >= ilo are in range
        n = 1 + (hi - ilo - 1) // i
        # Mark them as composite
        primes[ilo - lo:: i] = n * [False]
    return [i for i, v in enumerate(primes, lo) if v]


nb_items = int(input())

for i in range(nb_items):
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    primes = range_sieve(m, n+1)
    for j in primes:
        print(j)
    print("\n")
