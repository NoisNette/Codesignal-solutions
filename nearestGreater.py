def nearestGreater(a):
    b = [None] * len(a)
    stack = []
    
    for i in range(len(a)):
        
        while stack and a[stack[-1]] < a[i]:
            last_index = stack.pop()
            if b[last_index] == -1 or i - last_index < last_index - b[last_index]: 
                b[last_index] = i
        if not stack:
            b[i] = -1
        else:
            if a[stack[-1]] > a[i]:
                b[i] = stack[-1]
            else:
                b[i] = b[stack[-1]]
        stack.append(i)
    return b
