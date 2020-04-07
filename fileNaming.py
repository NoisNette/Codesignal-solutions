def fileNaming(names):
    if len(names) <= 1:
        return names
    been = []
    been.append(names[0])
    for i in range(1, len(names)):
        cur = names[i]
        if cur in been:
            idx = 1
            while True:
                fixed = cur + '(' + str(idx) + ')'
                if fixed not in been:
                    cur = fixed
                    break
                idx += 1
        been.append(cur)
        names[i] = cur
    return names
