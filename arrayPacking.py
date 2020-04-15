def arrayPacking(a):
    l = []
    for el in a:
        l.append((str(bin(el))[2:]).rjust(8, '0'))
    l.reverse()
    b = ''.join(l)
    return int(b, 2)
