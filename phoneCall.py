def phoneCall(a, b, c, d):
    d -= a + 9 * b
    return d // [c, b][d < 1] + 10
