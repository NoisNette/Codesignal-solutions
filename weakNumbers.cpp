vector<int> weakNumbers(int n) {
    using namespace std;
    vector<int> divisors(n, 0);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            if (i % j == 0) {
                divisors[i - 1]++;
            }
        }
    }
    vector<int> weaks(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (divisors[j] > divisors[i]) {
                weaks[i]++;
            }
        }
    }
    int best = *max_element(weaks.begin(), weaks.end()), count = 0;
    for (int i = 0; i < n; i++) {
        if (weaks[i] == best) {
            count++;
        }
    }
    return vector<int>{best, count};
}
