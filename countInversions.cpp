// 106 / 107 tests

int countInversions(vector<int> a) {
    using namespace std;
    int n = a.size();
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] > a[j]) {
                res++;
            }
        }
    }
    return res;
}
