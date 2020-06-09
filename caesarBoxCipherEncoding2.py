def caesarBoxCipherEncoding2(m):
      L = len(m)
      R = range(L)
      return sum([m[n*-~L//i%L*-~L//i%L] for n in R] == list(m) for i in R if i>1>L%i)
