def countNeighbouringPairs(s):
    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]: c += 1
    return c
