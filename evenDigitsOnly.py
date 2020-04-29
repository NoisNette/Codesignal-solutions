def evenDigitsOnly(n):
    for d in str(n):
        if int(d) % 2 == 1: return False
    return True
