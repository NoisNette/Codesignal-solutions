def divideAsLongAsPossible(n, d):

    while n % d == 0:
        n /= d
    return n
