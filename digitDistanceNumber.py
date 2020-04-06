def digitDistanceNumber(n):
    a = str(n)
    b = ""
    for i in range(len(a)-1):
        bd = abs(int(a[i+1]) - int(a[i]))
        b += str(bd)
    return int(b)
