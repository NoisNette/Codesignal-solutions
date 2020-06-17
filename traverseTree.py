def traverseTree(root):
    if root is None: 
        return []
    q = []
    res = []
    q.append(root) 
    while q: 
        count = len(q) 
        while count > 0: 
            temp = q.pop(0) 
            res.append(temp.value)
            if temp.left: 
                q.append(temp.left) 
            if temp.right: 
                q.append(temp.right) 
            count -= 1
    return res
