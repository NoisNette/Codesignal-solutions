def rotateImage(a):
    ans = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[j][i])
        ans.append(row[::-1])
    return ans
