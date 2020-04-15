def isInfiniteProcess(a, b):
    nr = 0;
    while a != b:
        nr += 1
        a += 1
        b -= 1
        if a > 500: return True
    return False
