def tennisSet(score1, score2):
    n1 = min(score1, score2)
    n2 = max(score1, score2)
    if n2 == 6: return n1 < 5
    return n2 == 7 and n1 >= 5 and n1 < n2
