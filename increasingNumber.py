def increasingNumber(x, n):
    for i in range(1, n + 1):
        while x % i:
            x += 1
    return x
