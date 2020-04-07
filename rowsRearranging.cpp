bool rowsRearranging(vector<vector<int>> matrix) {
    using namespace std;
    sort(matrix.begin(), matrix.end(), [] (auto row1, auto row2) {
        return row1 < row2;
    });
    for (int j = 0; j < matrix[0].size(); j++) {
        for (int i = 1; i < matrix.size(); i++) {
            if (matrix[i][j] <= matrix[i - 1][j]) {
                return false;
            }
        }
    }
    return true;
}
