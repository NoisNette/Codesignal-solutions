# 38 / 44 tests pass

def alternatingSort(a):
    n = len(a)
    i = 0
    j = -1
    if n == 1:
        return True
    elif n % 2 == 0:
        print('Even array')
        while i < n // 2:
            if a[i] > a[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    else:
        print('Odd array')
        while i < n // 2:
            print(i, j)
            if a[i] > a[j]:
                return False
            else:
                i += 1
                j -= 1
        print("one last comparison")
        print(i, i+1)
        if a[i] > a[i+1]:
            return True
        else:
            return False
