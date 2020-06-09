def findSquareSide(x, y):
    res, count = 0, 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dist = math.sqrt(dx * dx + dy * dy)
            sz = dist**2
            if count == 0:
                res = sz
                count += 1
            else:
                if res == sz: count += 1
                else: count -= 1
    return res
