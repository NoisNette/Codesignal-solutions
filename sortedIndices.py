def sortedIndices(a):
    indices = []
    for i in range(len(a)):
        indices.append(i)
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[indices[j]] > a[indices[j + 1]]:
                indices[j + 1], indices[j] = indices[j], indices[j + 1] 
    return indices
