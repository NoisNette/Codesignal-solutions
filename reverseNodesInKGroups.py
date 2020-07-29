def reverseNodesInKGroups(l, k):
    t = []
    i = 0
    aux = []
    while l:
        if i == k:
            t += aux[::-1]
            aux = []
            i = 0
        aux.append(l.value)
        i += 1
        l = l.next
    if i == k:
        t += aux[::-1]
    else:
        t += aux
    return t
