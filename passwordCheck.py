def passwordCheck(ps):
    return len(ps) >= 5 and True in [l.isupper() for l in ps] and True in [l.islower() for l in ps] and True in [l.isdigit() for l in ps]
