# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    l1 = []
    while l != None:
        l1.append(l.value)
        l = l.next
    
    l1.append(value)
    return sorted(l1)
