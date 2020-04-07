def isArithmeticProgression(sequence):
    if len(sequence) <= 1:
        return False
    diff = sequence[0] - sequence[1]
    for i in range(len(sequence)-1):
        if sequence[i + 1] != sequence[i] - diff:
            return False
    return True
