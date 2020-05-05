std::string smallestCyclicString(std::string inputString) {

  struct HashHelper {
    int P = 997;
    int M = 28001;
    std::vector<int> hash;
    std::vector<int> powP;

    HashHelper(std::string const & s) {
      hash.push_back(0);
      powP.push_back(1);
      for (int i = 1; i <= (int)s.size(); i++) {
        hash.push_back((hash[i - 1] * P + (int)s[i - 1]) % M);
        powP.push_back((powP[i - 1] * P) % M);
      }
    }

    // Hash of substring with indices [l, r)
    int substrHash(int l, int r) {
      return (hash[r] - (hash[l] * powP[r - l] % M) + M) % M;
    }
  };

  int n = inputString.size();
  inputString += inputString;
  HashHelper h(inputString);
  int bestShift = 0;
  for (int i = 1; i < n; i++) {
    int l = 0,
        r = n;
    while (r - l > 1) {
      int m = (l + r) / 2;
      if (h.substrHash(bestShift, bestShift + m) ==
          h.substrHash(i, i + m)) {
        l = m;
      } else {
        r = m;
      }
    }

    int commonPrefixLen = r;
    if (inputString[bestShift + commonPrefixLen] <
        inputString[i + commonPrefixLen]) {
      bestShift = i;
    }
  }

  return inputString.substr(bestShift, n);
}
