def stringReformatting(s, k):
    s = list(s.split('-'))
    s = ''.join(s)
    ans = [s[:len(s)%k]]
    s = s[len(s)%k:]
    while len(s) >= k:
        ans.append(s[:k])
        s = s[k:]
    if ans[0] == '':
        ans.pop(0)
    return '-'.join(ans)
