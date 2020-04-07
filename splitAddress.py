def splitAddress(address):
    add = address.split('/')
    ans = []
    if add[0][-1] == ':':
        add[0] = add[0][:-1]
    for i in range(len(add)):
        if '.com' in add[i]:
            add[i] = add[i][:-4]
    for i in range(len(add)):
        if add[i] != "":
            ans.append(add[i])
    return ans
