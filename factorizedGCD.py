def factorizedGCD(a, b):
    j = 0
    result = 1
    for i in range(len(a)):
        while j < len(b) and a[i] > b[j]:
            j += 1
        if j < len(b) and a[i] == b[j]:
            result *= a[i]
            j += 1
    return result
