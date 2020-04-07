vector<vector<int>> rotateImage(vector<vector<int>> a) {
    using namespace std;
    int n = a.size();
    for (int c = 1; c <= n / 2; c++) {
        for (int i = 1; i <= n - 2 * c + 1; i++) {
            swap(a[c - 1][c - 1 + i - 1], a[c - 1 + i - 1][n - c]);
        }
        for (int i = 1; i <= n - 2 * c + 1; i++) {
            swap(a[c - 1][c - 1 + i - 1], a[n - c][n - c - (i - 1)]);
        }
        for (int i = 1; i <= n - 2 * c + 1; i++) {
            swap(a[c - 1][c - 1 + i - 1], a[n - c - (i - 1)][c - 1]);
        }
    }
    return a;
}
