int firstOperationCharacter(string s) {
    using namespace std;
    int priority = 1;
    vector<pair<int, int>> v;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') priority += 2;
        else if (s[i] == ')') priority -= 2;
        else {
            if (s[i] == '+' || s[i] == '-') v.push_back(std::pair<int, int>(i, priority + 1));
            else if (s[i] == '*' || s[i] == '/') v.push_back(std::pair<int, int>(i, priority + 2));
        }
    }
    int res = 0;
    int maxPriority = 0;
    for (pair<int, int> p : v) {
        if (maxPriority < p.second) {
            res = p.first;
            maxPriority = p.second;
        }
    }
    return res;
}
