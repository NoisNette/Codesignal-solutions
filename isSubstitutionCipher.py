def isSubstitutionCipher(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
