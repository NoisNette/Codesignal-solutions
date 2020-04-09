# 75 / 80 tests


import itertools
def tripletSum(x, a):
    m = list( itertools.combinations(a, 3) )
    for item in m:
        if sum(item) == x:
            return True
    return False
