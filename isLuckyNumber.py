def isLuckyNumber(n):
    while n > 0:
        tmpDigit = n % 10
        if tmpDigit != 7 and tmpDigit != 4:
            return False
        n = n // 10
    return True
