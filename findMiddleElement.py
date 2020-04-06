def findMiddleElement(l):
    l1 = []
    while l!=None:
        l1.append(l.value)
        l = l.next
    return l1[len(l1)//2]
