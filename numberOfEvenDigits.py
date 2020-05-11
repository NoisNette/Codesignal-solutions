def numberOfEvenDigits(n):
    c = 0
    for i in str(n):
        if int(i) % 2 == 0: c += 1
    return c
