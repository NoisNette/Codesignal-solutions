def mirrorBits(a):
    b = bin(a)[2:]
    return int(b[::-1], 2)
