string amendTheSentence(string s) {
    using namespace std;
    regex reg("[A-Z]?[a-z]*");
    vector<string> items;
    for (auto it = sregex_iterator(s.begin(), s.end(), reg); it != sregex_iterator(); it++) {
        string item = it->str();
        if (item.size() == 0) {
            continue;
        }
        item[0] = tolower(item[0]);
        items.push_back(item);
    }
    string res = "";
    for (int i = 0; i < items.size(); i++) {
        if (i > 0) {
            res += " ";
        }
        res += items[i];
    }
    return res;
}
