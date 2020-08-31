def piecesOfDistinctLengths(strawLength):
    n = round((strawLength * 2)**.5)
    return n - 1 if n * (n + 1) / 2 > strawLength else n
