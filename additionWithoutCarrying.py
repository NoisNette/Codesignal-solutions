def additionWithoutCarrying(param1, param2):
    s = ""
    param1, param2 = str(param1), str(param2)
    p1 = param1.rjust(max(len(param1), len(param2)), '0')
    p2 = param2.rjust(max(len(param1), len(param2)), '0')
    for i in range(len(p1)):
        s += str((int(p1[i]) + int(p2[i])) % 10)
    return int(s)
