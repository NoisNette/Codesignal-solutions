def boxPiles(a):
    a = sorted(a)
    used = [False for j in range(len(a))]
    used_num = 0
    ans = 0
    while used_num < len(used):
        height = 0
        for i in range(len(a)):
            if a[i] >= height and not used[i]:
                height += 1
                used[i] = True
                used_num += 1
        ans += 1
    return ans
