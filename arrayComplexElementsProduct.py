def arrayComplexElementsProduct(real, imag):
  ans = [real[0], imag[0]]
  
  for i in range(1, len(real)):
    tmp = ans[0] * real[i] - ans[1] * imag[i]
    ans[1] = ans[1] * real[i] + ans[0] * imag[i]
    ans[0] = tmp
  return ans
