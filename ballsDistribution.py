def ballsDistribution(c, b, boxSize) {
    if b < boxSize: return b - c
    elif b == c and b > boxSize: return b
    else: return 0
