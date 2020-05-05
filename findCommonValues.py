def val(t,out):
    if t is None:
        return(out)
    else:
        out.append(t.value)
        out = out +val(t.left,[])+val(t.right,[])
    return(out)

def findCommonValues(t1, t2):
    s1 = set(val(t1,[]))
    s2 = set(val(t2,[]))
    return sorted(list(s1&s2))
