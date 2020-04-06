def theJanitor(word):
    a = [0]*26
    for i in set(word):
        a[ord(i)-97] = len(word)-word.index(i)-word[::-1].index(i)
    return a 
