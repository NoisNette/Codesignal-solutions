char firstNotRepeatingCharacter(string s) {
    using namespace std;
    int counts[26], poses[26];
    fill_n(counts, 26, 0);
    fill_n(poses, 26, -1);
    
    for (int i = 0; i < s.size(); i++) {
        char ch = s[i];
        counts[ch - 'a']++;
        poses[ch - 'a'] = i;
    }
    
    char res = '_';
    int min_pos = numeric_limits<int>::max();
    for (int i = 0; i < 26; i++) {
        if (counts[i] == 1) {
            char ch = 'a' + i;
            int pos = poses[i];
            if (pos < min_pos) {
                res = ch;
                min_pos = pos;
            }
        }
    }
    
    return res;
}
