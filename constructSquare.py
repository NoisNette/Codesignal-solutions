s, = eval(dir()[0])
i = l = -1
c = lambda s:sorted(map(s.count,s))
while i<4e4:
    i += 1
    if c(`i*i`)==c(s):
        l = i*i
return l
