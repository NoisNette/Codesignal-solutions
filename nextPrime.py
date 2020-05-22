def nextPrime(n):

    i = n + 1
    while True:
        isPrime = True
        divisor = 2
        while divisor * divisor <= i:
            if i % divisor == 0:
                isPrime = False
                break
            divisor += 1
        if isPrime:
            return i
        i += 1
