def amendTheSentence(s):
    ans = []
    for el in s:
        if el.isupper():
            ans.append(' ')
        ans.append(el.lower())
    return ''.join(ans).strip()
