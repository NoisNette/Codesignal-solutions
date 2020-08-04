def kthDigit(n, k):
    numDigits = 0
    number = n
    while number:
        numDigits += 1
        number //= 10

    indexFromLast = numDigits - k + 1

    while n:
        indexFromLast -= 1
        if indexFromLast == 0:
            return n % 10
        n //= 10

    return -1
