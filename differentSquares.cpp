int differentSquares(vector<vector<int>> matrix) {
    using namespace std;
    set<string> cache;
    for (int i = 0; i < matrix.size() - 1; i++) {
        for (int j = 0; j < matrix[i].size() - 1; j++) {
            string token = to_string(matrix[i][j]) + "-" +
                to_string(matrix[i][j + 1]) + "-" +
                to_string(matrix[i + 1][j]) + "-" +
                to_string(matrix[i + 1][j + 1]);
            cache.insert(token);
        }
    }
    return cache.size();
}
