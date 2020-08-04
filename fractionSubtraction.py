def fractionSubtraction(a, b):
    c = [a[0] * b[1] - a[1] * b[0], a[1] * b[1]]
    g = math.gcd(c[0], c[1])

    c[0] /= g
    c[1] /= g

    return c
