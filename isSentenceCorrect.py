def isSentenceCorrect(sentence):
    pattern = "^[A-Z][^.?!]*[.?!]$"
    return re.match(pattern, sentence) is not None
