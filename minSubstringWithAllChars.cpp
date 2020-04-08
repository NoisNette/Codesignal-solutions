string minSubstringWithAllChars(string s, string t) {
    int n = s.size();
    int m = -1, ind = 0;
    for (int i = 0; i < n; ++i) {
        int left = t.size(), len = 0;
        vector<bool> got(26,true);
        for (auto c : t)
            got[c-'a'] = false;
        for (int j = i; j < s.size() && left; ++j, ++len)
            if (!got[s[j]-'a'])
                got[s[j]-'a'] = true, --left;
        if (left)
            break;
        if (m == -1 || len < m)
            m = len, ind = i;
    }
    return s.substr(ind,m);
}
