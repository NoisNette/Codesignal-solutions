def lastDigit(a, b):
    result = 1
    for i in range(b):
        result = result*a%10
    return result
