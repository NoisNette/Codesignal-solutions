int sumOfSquares(int n) {
  int res = 0;
  for (int i = 1; i <= n; i++) {
    res += i * i;
  }
  return res;
}
