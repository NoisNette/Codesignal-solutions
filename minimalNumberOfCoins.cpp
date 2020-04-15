int minimalNumberOfCoins(std::vector<int> coins, int price) {
    int res = 0;
    reverse(coins.begin(), coins.end());
    for (auto coin: coins) {
        if (price <= 0) {
            break;
        }
        res += price / coin;
        price -= price / coin * coin;
    }
    return res;
}
