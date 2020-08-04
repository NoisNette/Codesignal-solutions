def fibonacciSum(n):

    fib = []
    fib0 = 1
    fib1 = 1
    fib.append(fib1)
    while fib1 < n:
        fib2 = fib0 + fib1
        fib.append(fib2)
        fib0 = fib1
        fib1 = fib2

    ans = []
    for i in range(len(fib) - 1, -1, -1):
        if n >= fib[i]:
            n -= fib[i]
            ans.append(fib[i])

    return list(reversed(ans))
