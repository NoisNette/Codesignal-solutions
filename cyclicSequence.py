def cyclicSequence(sequence):
    found = False
    st = -1
    for i in range(1, len(sequence)):
        if sequence[i - 1] == sequence[i]:
            return False
        if sequence[i - 1] > sequence[i]:
            if found:
                return False
            found = True
            st = i
    return st != -1 and sequence[0] > sequence[len(sequence) - 1] or st == -1
