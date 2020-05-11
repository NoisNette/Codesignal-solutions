def fractionComparison(a, b):
    if a[0] / a[1] > b[0]/b[1]: return '>'
    elif a[0] / a[1] < b[0]/b[1]: return '<'
    else: return '='
