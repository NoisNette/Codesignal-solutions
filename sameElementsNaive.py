def sameElementsNaive(a, b):
    return sum(1 for i in a if i in b)
