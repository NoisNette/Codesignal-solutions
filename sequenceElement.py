def sequenceElement(a, n):
    if len(a) - 1 >= n:
        return a[n]
    tmp = ''.join(str(v) for v in a)
    cnt = 0
    while cnt < 4686:
        cnt += 1
        i = len(a)
        curr = (a[i - 5] + a[i - 4] + a[i - 3] + a[i - 2] + a[i - 1]) % 10
        a.append(curr)

    loop = ''.join(str(v) for v in a)[:4686]
    return int(loop[n % (len(loop))])
