vector<vector<int>> minesweeper(vector<vector<bool>> matrix) {
    using namespace std;
    vector<vector<int>> res;
    int m = matrix.size(), n = matrix[0].size();
    for (int i = 0; i < m; i++) {
        vector<int> row;
        for (int j = 0; j < n; j++) {
            int count = 0;
            for (int i1 = -1; i1 <= 1; i1++) {
                for (int j1 = -1; j1 <= 1; j1++) {
                    int i2 = i + i1, j2 = j + j1;
                    if (i2 == i && j2 == j) {
                        continue;
                    }
                    if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n) {
                        count += matrix[i2][j2] ? 1 : 0;
                    }
                }
            }
            row.push_back(count);
        }
        res.push_back(row);
    }
    return res;
}
