def isIncreasingDigitsSequence(n):
    a = [int(i) for i in str(n)]
    return all([a[i] < a[i+1] for i in range(len(a) - 1)])
