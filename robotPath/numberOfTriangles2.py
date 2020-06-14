from itertools import combinations
def numberOfTriangles2(sticks):
    lst = list(combinations(sticks, 3))
    count = 0
    for el in lst:
        if el[0] + el[1] > el[2] and el[1] + el[2] > el[0] and el[2] + el[0] > el[1]: count += 1
    return count
