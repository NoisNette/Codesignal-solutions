def possibleSums(coins, quantity):
    p = {0}
    for c, q in zip(coins, quantity):
        p = {x + c * i for x in p for i in range(q + 1)}
    
    return len(p) - 1
