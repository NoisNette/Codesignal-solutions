# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeDiameter(t):
    d = btDiameter(t)
    return d[1]


def btDiameter(t): 
    if(t == None) :return [0,0]
    
    L = btDiameter(t.left)
    R = btDiameter(t.right)
    
    ML = 1+max(L[0],R[0])
    MD = max(1+L[0]+R[0], max(L[1],R[1]))
    return [ML, MD ]
