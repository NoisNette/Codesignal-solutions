def higherVersion(ver1, ver2):
    a = ver1.split('.')
    b = ver2.split('.')
    for i in range(len(a)):
        cmp_ = int(a[i]) - int(b[i])
        if cmp_ > 0:
            return True
        elif cmp_ < 0:
            return False
    return False
