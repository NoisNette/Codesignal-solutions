from fractions import Fraction
def fractionSum(a, b):
    x = str(Fraction(a[0], a[1]) + Fraction(b[0], b[1]))
    if '/' not in x:
        return [int(x), 1]
    return [int(x.split('/')[0]), int(x.split('/')[1])]
