def largestDistance(a):
    res = -1000
    for i in range(len(a) // 2):
        x1 = a[2 * i]
        y1 = a[2 * i + 1]
        for j in range(i + 1, len(a) // 2):
            x2 = a[2 * j]
            y2 = a[2 * j + 1]
            dist = max(abs(x1 - x2), abs(y1 - y2))
            res = max(res, dist)
    return res
