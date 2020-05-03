def niceFractions2(n):
    res = 0
    i = 0
    while i * n < 10 ** 5:
        digits = [False] * 10
        a = i * n
        b = i
        isNice = True
        for j in range(5):
            digits[a % 10] = True
            a //= 10
            digits[b % 10] = True
            b //= 10
        for j in range(10):
            if not digits[j]:
                isNice = False
                break
        if isNice:
            res += 1
        i += 1
    return res
