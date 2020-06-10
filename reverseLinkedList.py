def reverseLinkedList(l):
    lst = []
    while l:
        lst.append(l.value)
        l = l.next
    return lst[::-1]
