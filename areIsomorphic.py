def areIsomorphic(array1, array2):
    if len(array1) != len(array2): return False
    for i in range(len(array1)):
        if len(array1[i]) != len(array2[i]): return False
    return True
