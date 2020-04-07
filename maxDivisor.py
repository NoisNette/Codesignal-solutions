def maxDivisor(left, right, divisor):
    i = right
    while i >= left:
        if i % divisor == 0:
            return i
        i -= 1
    return -1
