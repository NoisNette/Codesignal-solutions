def equationTemplate(values):
    a, b, c, d = sorted(values)
    return a==b*c*d or a*b==c*d or a*b*c==d or a*d==b*c or a*c==b*d
