vector<int> maxSumSegments(vector<int> inputArray) {
    using namespace std;
    vector<int> res;
    int n = inputArray.size();
    for (int len = 1; len <= n; len++) {
        int sum = 0, best, best_i;
        for (int i = 0; i < len; i++) {
            sum += inputArray[i];
        }
        best = sum;
        best_i = 0;
        for (int i = 1; i + len <= n; i++) {
            sum -= inputArray[i - 1];
            sum += inputArray[i + len - 1];
            if (sum > best) {
                best = sum;
                best_i = i;
            }
        }
        res.push_back(best_i);
    }
    return res;
}
