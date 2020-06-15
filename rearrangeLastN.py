def rearrangeLastN(l, n):
    l1 = []
    while l:
        l1 += l.value,
        l = l.next
    return l1[-n:] + l1[:-n]
