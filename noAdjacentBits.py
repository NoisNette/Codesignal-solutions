def noAdjacentBits(a):

    lastBit = 0
    idx = 0
    while (1 << idx) <= a:
        curBit = (a >> idx) & 1
        if lastBit == 1 and curBit == 1:
            return False
        lastBit = curBit
        idx += 1

    return True
