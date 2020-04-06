def onlyEvenNumbers(left, right):
    l = []
    for i in range(left, right+1):
        if i % 2 == 0:
            l.append(i)
    return l
