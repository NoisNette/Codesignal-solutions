set<int> sums(vector<int> coins, vector<int> quantity) {
    using namespace std;
    if (quantity.size() == 0) {
        return {};
    }
    vector<int> remain_coins{coins.begin() + 1, coins.end()};
    vector<int> remain_quantity{quantity.begin() + 1, quantity.end()};
    auto remain_sums = sums(remain_coins, remain_quantity);
    set<int> res;
    if (remain_sums.size() == 0) {
        int q = quantity[0];
        for (int i = 0; i <= q; i++) {
            res.insert(i * coins[0]);
        }
        return res;
    }
    int q = quantity[0];
    for (int i = 0; i <= q; i++) {
        for (auto num: remain_sums) {
            res.insert(num + i * coins[0]);
        }
    }
    return res;
}

int possibleSums(vector<int> coins, vector<int> quantity) {
    using namespace std;
    return sums(coins, quantity).size() - 1;
}
