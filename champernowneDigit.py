def champernowneDigit(n):
    c = ""
    for i in range(1, n + 1):
        c += str(i)
    return int(c[n-1])
