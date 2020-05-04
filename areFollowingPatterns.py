o = eval(dir()[0])
return len({len({*a}) for a in o + [zip(*o)]}) < 2
