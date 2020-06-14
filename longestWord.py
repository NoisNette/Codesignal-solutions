def longestWord(text):
    answer = ''
    current = []
    for i in range(len(text)):
        if ('a' <= text[i] and text[i] <= 'z'
                or 'A' <= text[i] and text[i] <= 'Z'):
            current.append(text[i])
            if len(current) > len(answer):
                answer = ''.join(current)
        else:
            current = []
    return ''.join(answer)
