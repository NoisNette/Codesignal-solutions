n, = eval(dir()[0])
r = [[n, 1]]
def f(d, n, *a):
    n > 1 or r.append(a)
    while d > 1:
        n % d or f(d, n / d, *a, d)
        d -= 1
f(n - 1, n)
return r
