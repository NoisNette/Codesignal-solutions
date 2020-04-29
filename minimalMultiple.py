def minimalMultiple(divisor, lowerBound):
    ans = 0
    while ans < lowerBound:
        ans += divisor
    return ans
