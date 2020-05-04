def pagesNumberingWithInk(current, numberOfDigits):

    def countDigitsInNumber(n):
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count
    digitsInCurrent = countDigitsInNumber(current)
    while numberOfDigits >= digitsInCurrent:
        numberOfDigits -= digitsInCurrent
        current += 1
        digitsInCurrent = countDigitsInNumber(current)
    return current - 1
