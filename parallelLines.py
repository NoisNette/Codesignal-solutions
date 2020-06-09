def parallelLines(line1, line2):
    a1 = line1[0]
    b1 = line1[1]
    a2 = line2[0]
    b2 = line2[1]
    return a1 * b2 == a2 * b1
