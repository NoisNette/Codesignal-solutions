int missingNumber(vector<int> arr) {
    using namespace std;
    int n = arr.size();
    set<int> cache;
    for (auto num: arr) {
        cache.insert(num);
    }
    for (int i = 0; i <= n; i++) {
        if (cache.find(i) == cache.end()) {
            return i;
        }
    }
    return -1;
}
