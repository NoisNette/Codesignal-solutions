int countTriangles(vector<int> x, vector<int> y) {
    using namespace std;
    int res = 0, n = x.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if ((x[i] - x[j]) * (y[i] - y[k]) - (x[i] - x[k]) * (y[i] - y[j]) != 0) {
                    res++;
                }
            }
        }
    }
    return res;
}
