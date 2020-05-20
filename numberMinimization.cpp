std::set<std::vector<int>> cache;
int numberMinimization(int n, int d) {
    using namespace std;
    string item = to_string(n);
    sort(item.begin(), item.end());
    int res = stoi(item);
    do {
        int n1 = stoi(item);
        if (n1 % d == 0 && cache.find({d, n1}) == cache.end()) {
            cache.insert({d, n1});
            res = min(res, numberMinimization(n1 / d, d));
        }
    } while (next_permutation(item.begin(), item.end()));
    return res;
}
