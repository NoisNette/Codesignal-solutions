def toDecimal(k, n):
    result = 0
    power = 1
    for i in range(len(n) - 1, -1, -1):
        result += int(n[i]) * power
        power *= k
    return result
