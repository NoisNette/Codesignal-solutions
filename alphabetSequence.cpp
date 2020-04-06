bool alphabetSubsequence(string s) {
    using namespace std;
    char pre = s[0];
    if (pre < 'a' || pre > 'z') {
        return false;
    }
    for (int i = 1; i < s.size(); i++) {
        char ch = s[i];
        if (ch < 'a' || ch > 'z') {
            return false;
        }
        if (ch <= pre) {
            return false;
        }
        pre = ch;
    }
    return true;
}
