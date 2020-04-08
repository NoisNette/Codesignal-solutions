def fillingBlocks(n):
    f = [1, 5]
    a = [1, 2]
    b = [1, 1]

    for _ in range(3,n+1):

        an = f[-1] + a[-1]
        bn = f[-1] + b[-2]

        fn = f[-2] + f[-1] + 2*a[-1] + b[-1]

        f += [fn]
        a += [an]
        b += [bn]
        
    return f[n-1]
