bool unusualDictionary(vector<string> wordList) {
    using namespace std;
    vector<string> sorted(wordList.begin(), wordList.end());
    sort(sorted.begin(), sorted.end(), [] (auto item1, auto item2) {
        string h1 = "", t1 = item1;
        int idx1;
        if ((idx1 = item1.find(" ")) != string::npos) {
            h1 = item1.substr(0, idx1);
            t1 = item1.substr(idx1 + 1);
        }
        string h2 = "", t2 = item2;
        int idx2;
        if ((idx2 = item2.find(" ")) != string::npos) {
            h2 = item2.substr(0, idx2);
            t2 = item2.substr(idx2 + 1);
        }
        if (t1 != t2) {
            return t1 < t2;
        }
        if (h1.size() > 0 && h2.size() > 0) {
            return h1 < h2;
        }
        return item1 < item2;
    });
    return sorted == wordList;
}
