def nextLarger(a):
    b = []
    for i in range(len(a)):
        l = len(b)
        for j in range(i, len(a)):
            if a[j] > a[i]:
                b.append(a[j])
                break
        if l == len(b): b.append(-1)
    return b
