def sameDigitNumber(n):
    digit = n % 10
    while n != 0:
        if n % 10 != digit:
            return False
        n //= 10
    return True
