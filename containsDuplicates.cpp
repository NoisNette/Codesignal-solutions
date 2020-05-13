bool containsDuplicates(vector<int> a) {
    using namespace std;
    set<int> cache;
    for (auto num: a) {
        if (cache.find(num) != cache.end()) {
            return true;
        }
        cache.insert(num);
    }
    return false;
}
