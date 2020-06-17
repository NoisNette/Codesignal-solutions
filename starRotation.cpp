vector<vector<int>> getRowIndex1(vector<vector<int>> matrix, int width, vector<int> center) {
    using namespace std;
    int w = width / 2;
    vector<vector<int>> res(width);
    int x = center[0] - w, y = center[1];
    for (int i = 0; i < width; i++) {
        res[i] = vector<int>{x + i, y};
    }
    return res;
}

vector<vector<int>> getRowIndex2(vector<vector<int>> matrix, int width, vector<int> center) {
    using namespace std;
    int w = width / 2;
    vector<vector<int>> res(width);
    int x = center[0] - w, y = center[1] + w;
    for (int i = 0; i < width; i++) {
        res[i] = vector<int>{x + i, y - i};
    }
    return res;
}

vector<vector<int>> getRowIndex3(vector<vector<int>> matrix, int width, vector<int> center) {
    using namespace std;
    int w = width / 2;
    vector<vector<int>> res(width);
    int x = center[0], y = center[1] + w;
    for (int i = 0; i < width; i++) {
        res[i] = vector<int>{x, y - i};
    }
    return res;
}

vector<vector<int>> getRowIndex4(vector<vector<int>> matrix, int width, vector<int> center) {
    using namespace std;
    int w = width / 2;
    vector<vector<int>> res(width);
    int x = center[0] + w, y = center[1] + w;
    for (int i = 0; i < width; i++) {
        res[i] = vector<int>{x - i, y - i};
    }
    return res;
}

vector<vector<int>> rotate(vector<vector<int>> matrix, int width, vector<int> center) {
    using namespace std;
    vector<vector<vector<int>>> rowIndexs(4);
    rowIndexs[0] = getRowIndex1(matrix, width, center);
    rowIndexs[1] = getRowIndex2(matrix, width, center);
    rowIndexs[2] = getRowIndex3(matrix, width, center);
    rowIndexs[3] = getRowIndex4(matrix, width, center);
    vector<vector<int>> rows(4);
    for (int k = 0; k < 4; k++) {
        vector<vector<int>> rowIndex = rowIndexs[k];
        vector<int> row(width);
        for (int i = 0; i < width; i++) {
            row[i] = matrix[rowIndex[i][0]][rowIndex[i][1]];
        }
        rows[k] = row;
    }
    for (int k = 0; k < 1; k++) {
        vector<vector<int>> rowIndex = rowIndexs[k];
        vector<int> row = rows[4 - 1 - k];
        for (int i = 0; i < width; i++) {
            matrix[rowIndex[width - 1 - i][0]][rowIndex[width - 1 - i][1]] = row[i];
        }
    }
    for (int k = 1; k < 4; k++) {
        vector<vector<int>> rowIndex = rowIndexs[k];
        vector<int> row = rows[k - 1];
        for (int i = 0; i < width; i++) {
            matrix[rowIndex[i][0]][rowIndex[i][1]] = row[i];
        }
    }
    return matrix;
}

vector<vector<int>> starRotation(vector<vector<int>> matrix, int width, vector<int> center, int t) {
    using namespace std;
    t = t % 8;
    for (int i = 0; i < t; i++) {
        matrix = rotate(matrix, width, center);
    }
    return matrix;
}
