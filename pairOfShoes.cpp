bool pairOfShoes(vector<vector<int>> shoes) {
    using namespace std;
    map<int, int> cache;
    for (auto pair: shoes) {
        int type = pair[0], size = pair[1];
        if (cache.find(size) == cache.end()) cache[size] = 0;
        if (type == 0) cache[size]--;
        else cache[size]++;
    }
    for (auto pair: cache) if (pair.second != 0) return false;
    return true;
}
