vector<int> gravitation(vector<string> rows) {
    using namespace std;
    int m = rows.size(), n = rows[0].size();
    vector<int> res;
    while (true) {
        for (int j = 0; j < n; j++) {
            int c = 0;
            for (int i = m - 2; i >= 0; i--) {
                if (rows[i][j] == '#' && rows[i + 1][j] == '.') {
                    swap(rows[i][j], rows[i + 1][j]);
                    c++;
                }
            }
            if (c == 0) {
                res.push_back(j);
            }
        }
        if (res.size() > 0) {
            break;
        }
    }
    return res;
}
