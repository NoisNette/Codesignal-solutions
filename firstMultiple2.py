def firstMultiple2(divisors, start):
    i = start
    while True:
        for j in range(len(divisors)):
            if i % divisors[j] == 0: return i
        i += 1
