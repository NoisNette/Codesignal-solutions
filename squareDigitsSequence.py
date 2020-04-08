def squareDigitsSequence(a0):

    cur = a0
    was = set()

    while not (cur in was):
        was.add(cur)
        nxt = 0
        while cur > 0:
            nxt += (cur % 10) * (cur % 10)
            cur //= 10
        cur = nxt

    return len(was) + 1
