def rangeBitCount(a, b):
    ans = 0
    for i in range(a, b+1):
        ans += bin(i)[2:].count('1')
    return ans
