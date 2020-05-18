# Not tested on full suite, all test cases pass


def reversedSumOfDigits(p, n):
    if p == 0 and n != 1: return '-1'
    elif p == 0 and n == 1: return '0'
    for i in range(10**(n-1), 10**n):
        x = str(i)
        s = 0
        for j in x: s += int(j)
        if s == p: return str(i)
    return '-1'
