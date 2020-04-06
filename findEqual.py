def findEqual(sequence):
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] == sequence[j]:
                return True
            j += 1
    return False
