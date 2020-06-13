def create2DArray(lengths):
    ans = []
    for l in lengths:
        row = []
        for i in range(l): row.append(i)
        ans.append(row)
    return ans
