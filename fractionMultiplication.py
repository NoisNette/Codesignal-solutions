import math
def fractionMultiplication(a, b):
    n1 = a[0] * b[0]
    n2 = a[1] * b[1]
    g = math.gcd(max(n1, n2), min(n1, n2))
    return [n1 / g, n2 / g]
