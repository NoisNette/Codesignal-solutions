def axisAlignedCirclesBoundingBox(x, y, r):
    minX = x[0] - r[0]
    maxX = x[0] + r[0]
    minY = y[0] - r[0]
    maxY = y[0] + r[0]

    for i in range(1, len(x)):
        minX = min(x[i] - r[i], minX)
        maxX = max(x[i] + r[i], maxX)
        minY = min(y[i] - r[i], minY)
        maxY = max(y[i] + r[i], maxY)

    return (maxX - minX) * (maxY - minY)
