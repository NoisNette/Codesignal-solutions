def classifyStrings(s):
    if re.search(r"[aeiou]{3}|[^aeiou?]{5}", s):
        return "bad"
    if "?" not in s:
        return "good"
    a = classifyStrings(s.replace("?", "a", 1))
    b = classifyStrings(s.replace("?", "b", 1))
    return "mixed" if a != b else a
