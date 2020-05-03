def isGeometricProgression(sequence):

    for i in range(2, len(sequence)):
        if sequence[i] * sequence[0] != sequence[i - 1] * sequence[1]:
            return False
    return True
