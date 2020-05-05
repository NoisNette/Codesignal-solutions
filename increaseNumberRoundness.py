def increaseNumberRoundness(n):

    gotToSignificant = False
    while n > 0:
        if n % 10 == 0 and gotToSignificant:
            return True
        elif n % 10 != 0:
            gotToSignificant = True
        n //= 10

    return False
