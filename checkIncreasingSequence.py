def checkIncreasingSequence(seq):
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]: return False
    return True
