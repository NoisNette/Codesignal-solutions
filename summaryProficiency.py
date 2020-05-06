def summaryProficiency(a, n, m):

    result = 0
    i = 0
    while n > 0:
        if a[i] >= m:
            result += a[i]
            n -= 1
        i += 1

    return result
