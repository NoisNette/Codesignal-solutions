def pointInLine(point, line):
    x = point[0]
    y = point[1]
    a = line[0]
    b = line[1]
    c = line[2]
    return a * x + b * y + c == 0
