import math
def eulersTotientFunction(n):
    res = 0
    for i in range(1, n+1):
        if math.gcd(n, i) == 1:
            res += 1
    return res
