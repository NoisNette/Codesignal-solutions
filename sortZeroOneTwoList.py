def sortZeroOneTwoList(l):
    li = []
    while l:
        li.append(l.value)
        l = l.next
    li.sort()
    return li
