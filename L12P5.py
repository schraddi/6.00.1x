def genPrimes():
    allPrimes = []
    i = 1
    while True:
        i += 1
        isPrime = True
        for prime in allPrimes:
            if i%prime == 0:
                isPrime = False
                break
        if isPrime:
            allPrimes.append(i)
            yield i

primes = genPrimes()
for i in range (5):
    print primes.next()