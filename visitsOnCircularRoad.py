def visitsOnCircularRoad(n, visitsOrder):

    current = 1
    res = 0
    for i in range(len(visitsOrder)):
        res += min(abs(visitsOrder[i] - current),
                  n - abs(visitsOrder[i] - current))
        current = visitsOrder[i]
    return res
