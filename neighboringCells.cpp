std::vector<std::vector<int>> neighboringCells(std::vector<std::vector<int>> matrix) {
    for (int i = 0; i < matrix.size(); i++){
        for (int j = 0; j < matrix[i].size(); j++){
            if (matrix[i][j] != 0) continue;
            int n = 4;
            if (i == 0) n--;
            if (i == matrix.size()-1) n--;
            if (j == 0) n--;
            if (j == matrix[i].size()-1) n--;
            matrix[i][j] = n;
        }
    }
    return matrix;
}
