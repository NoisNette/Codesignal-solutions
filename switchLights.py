def switchLights(a):
    a[0] = 0
    for i in range(1, len(a)):
        if a[i] == 1:
            for j in range(i, -1, -1):
                a[j] = int(not a[j])
    return a
