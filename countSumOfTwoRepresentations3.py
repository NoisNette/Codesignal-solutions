def countSumOfTwoRepresentations3(n, l, r):
    n1 = max(l, n - r)
    n2 = min(n // 2, r)
    return max(n2 - n1 + 1, 0)
