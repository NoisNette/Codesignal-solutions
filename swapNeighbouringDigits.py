def swapNeighbouringDigits(n):
    n = list(str(n))
    for i in range(0, len(n) - 1, 2):
        n[i], n[i+1] = n[i+1], n[i]
    return int(''.join(n))
