int maximumSubsetProduct(std::vector<int> a) {
    using namespace std;
    if (a.size() == 1) {
        return 1;
    }
    int neg = 0, max_neg = numeric_limits<int>::min();
    for (auto num: a) {
        if (num < 0) {
            neg++;
            max_neg = max(max_neg, num);
        }
    }
    if (neg % 2 == 0) {
        return 1;
    }
    return max_neg;
}
