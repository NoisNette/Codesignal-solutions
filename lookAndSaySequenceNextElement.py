def lookAndSaySequenceNextElement(element):
    element += ' '
    pre = ' '
    count = 0
    res = ""
    for ch in element:
        if ch == pre:
            count += 1
        else:
            if count != 0:
                res += str(count) + pre
            pre = ch
            count = 1
    return res
