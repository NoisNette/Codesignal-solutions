def regexMatching(pattern, test):
    if pattern.startswith('^'):
        pattern = pattern[1:]
        return test.startswith(pattern)
    elif pattern.endswith('$'):
        pattern = pattern[:-1]
        return test.endswith(pattern)
    else:
        return pattern in test
