int commonCharacterCount(std::string s1, std::string s2) {
    std::map<char, int> cache1, cache2;
    for (auto ch: s1) {
        if (cache1.find(ch) == cache1.end()) {
            cache1[ch] = 0;
        }
        cache1[ch]++;
    }
    for (auto ch: s2) {
        if (cache2.find(ch) == cache2.end()) {
            cache2[ch] = 0;
        }
        cache2[ch]++;
    }
    int res = 0;
    for (auto pair: cache1) {
        char ch = pair.first;
        int count = pair.second;
        if (cache2.find(ch) != cache2.end()) {
            res += min(count, cache2[ch]);
        }
    }
    return res;
}
