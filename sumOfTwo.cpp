bool sumOfTwo(vector<int> a, vector<int> b, int v) {
    using namespace std;
    set<int> cache;
    for (auto num: a) {
        cache.insert(num);
    }
    for (auto n1: b) {
        int n2 = v - n1;
        if (cache.find(n2) != cache.end()) {
            return true;
        }
    }
    return false;
}
