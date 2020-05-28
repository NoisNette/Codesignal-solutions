def sumOfMultiples(n, k):
    m = n // k
    if m == 0: return 0
    return m * (m + 1) / 2 * k
