int giftSafety(string gift) {
    using namespace std;
    int res = 0, n = gift.size();
    for (int i = 0; i + 2 < n; i++) {
        set<char> cache;
        cache.insert(gift[i]);
        cache.insert(gift[i + 1]);
        cache.insert(gift[i + 2]);
        if (cache.size() < 3) {
            res++;
        }
    }
    return res;
}
