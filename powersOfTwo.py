def powersOfTwo(n):
    res = []
    base = 1
    while n > 0:
        if n % 2 == 1: res.append(base)
        base *= 2
        n //= 2
    return res
