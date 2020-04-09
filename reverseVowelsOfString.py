def reverseVowelsOfString(s):
    vowels = 'aeiouAEIOU'
    order = []
    ans = ""
    for l in s:
        if l in vowels:
            order.append(l)
    order.reverse()
    idx = 0
    for l in s:
        if l in vowels:
            ans += order[idx]
            idx += 1
        else:
            ans += l
    return ans
