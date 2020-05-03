int maximumSum(vector<int> a, vector<vector<int>> q) {
    using namespace std;
    int n = a.size();
    vector<int> counts(n, 0);
    for (auto query: q) {
        for (int i = query[0]; i <= query[1]; i++) {
            counts[i]++;
        }
    }
    sort(counts.begin(), counts.end());
    sort(a.begin(), a.end());
    int sum = 0;
    for (int i = n - 1; i >= 0; i--) {
        sum += counts[i] * a[i];
    }
    return sum;
}
