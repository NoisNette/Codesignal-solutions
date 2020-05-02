def isLucky(n):
    n = str(n)
    half = int(len(n)/2 + 1)
    h1 = n[:half-1]
    h2 = n[half-1:]
    s1 = 0
    s2 = 0
    for d in h1: s1 += int(d)
    for d in h2: s2 += int(d)
    return s1 == s2
