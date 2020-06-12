def isPangram(sentence):
    found = []
    result = True
    for i in range(26):
        found.append(False)
    for i in range(len(sentence)):
        code = ord(sentence[i])
        if ord('A') <= code and code <= ord('Z'):
            code += ord('a') - ord('A')
        if ord('a') <= code and code <= ord('z'):
            found[code - ord('a')] = True
    for i in range(26):
        if not found[i]:
            result = False
    return result
