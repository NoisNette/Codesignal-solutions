def amendTheSentence(s):
    l = list(s)
    ans = []
    for el in l:
        if el.isupper():
            ans.append(' ')
        ans.append(el.lower())
    return ''.join(ans).strip()
