std::vector<int> directionOfReading(std::vector<int> numbers) {
  vector<string> v;
  for (int p : numbers) {
    v.push_back(to_string(p));
  }
  for (string& s : v) {
    while ((int) s.length() < (int) numbers.size()) s = '0' + s;
  }
  vector<int> res;
  int n = numbers.size();
  for (int i = 0; i < n; i++) {
    int cur = 0;
    for (int j = 0; j < n; j++) {
      cur = cur * 10 + (v[j][i] - '0');
    }
    res.push_back(cur);
  }
  return res;
}
