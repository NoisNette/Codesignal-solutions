int numbersGrouping(vector<int> a) {
    using namespace std;
    set<int> groups;
    for (int num: a) {
        int group = (num - 1) / 10000;
        groups.insert(group);
    }
    return a.size() + groups.size();
}
