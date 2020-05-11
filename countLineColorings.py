def countLineColorings(points, colors):
    res = colors
    for i in range(1, points): res *= colors - 1
    return res
