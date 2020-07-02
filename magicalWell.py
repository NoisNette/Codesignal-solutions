def magicalWell(a, b, n):
    ans = 0
    while n:
        ans += (a * b)
        a += 1
        b += 1
        n -= 1
    return ans
