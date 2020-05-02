int createAnagram(std::string s, std::string t) {
    int countS[26] = {0}, countT[26] = {0};
    for (int i = 0; i < s.length(); i++) {
        countS[s[i] - 'A']++;
        countT[t[i] - 'A']++;
    }
    int res = 0;
    for (int i = 0; i < 26; i++) {
        int diff = countS[i] - countT[i];
        if (diff > 0) res += diff;
    }
    return res;
}
