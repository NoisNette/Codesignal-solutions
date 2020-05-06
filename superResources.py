def superResources(requests):

    def le(a, b):
        return int(a) <= int(b)

    if len(requests) < 2:
        return requests
    parts = [
            requests[0 : len(requests) // 2],
            requests[len(requests) // 2 : len(requests)]
    ]
    parts[0] = superResources(parts[0])
    parts[1] = superResources(parts[1])

    result = []
    idx = [0, 0]
    length = [len(parts[0]), len(parts[1])]
    last = None
    while idx[0] < length[0] or idx[1] < length[1]:
        if (idx[1] >= length[1] or idx[0] < length[0] and
                le(parts[0][idx[0]][0], parts[1][idx[1]][0])):
            k = 0
        else:
            k = 1
        element = parts[k][idx[k]]
        idx[k] += 1
        if element[0] != last:
            result.append(element)
            last = element[0]

    return result
