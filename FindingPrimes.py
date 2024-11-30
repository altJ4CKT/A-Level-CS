def PrimeNumbers(lim):
    primes = [2, 3, 5, 7, 9]
    notPrimes = []
    for i in range(2, lim):
        for j in range(2, i):
            if i % j == 0:
                notPrimes.append(i)
                break
        else:
            primes.append(i)
    return primes

print(PrimeNumbers(100))
        
