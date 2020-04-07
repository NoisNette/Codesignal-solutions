def meanGroups(a):
    means = []
    for group in a:
        mean = sum(group) / len(group)
        means.append(mean)
    singles = []
    for mean in means:
        if mean not in singles:
            singles.append(mean)
    ans = []
    for i in range(len(singles)):
        mns = []
        for j in range(len(means)):
            if singles[i] == means[j]:
                mns.append(j)
        ans.append(mns)
    return ans
