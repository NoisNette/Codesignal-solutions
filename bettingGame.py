def bettingGame(l):

    s = 0
    for i in range(len(l)):
        s += l[i]
    if s == 0:
        return False

    return s % len(l) == 0
