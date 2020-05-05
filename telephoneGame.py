def telephoneGame(messages):
    for i in range(1, len(messages)):
        if messages[i] != messages[i-1]: return i
    return -1
