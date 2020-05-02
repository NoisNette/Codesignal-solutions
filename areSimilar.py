def areSimilar(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]: count += 1
        if a[i] not in b or b[i] not in a: return False
    return count <= 2
