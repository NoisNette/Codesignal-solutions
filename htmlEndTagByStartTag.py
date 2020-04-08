def htmlEndTagByStartTag(t):
    s = t.split(' ')
    out = s[0]
    out = out.replace('<','</')
    out = out.replace('>','')
    return(out+'>')
