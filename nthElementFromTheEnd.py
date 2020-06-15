def nthElementFromTheEnd(l, n):
    l1 = []
    while l:
        l1.append(l.value)
        l = l.next
    if len(l1) < n: return -1
    return l1[-n]
