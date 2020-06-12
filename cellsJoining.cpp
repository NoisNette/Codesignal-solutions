vector<string> cellsJoining(vector<string> table, const vector<vector<int> >& coords) {
    using namespace std;
    vector<int> cols;
    vector<int> rows;
    const size_t width = table[0].length();
    const size_t height = table.size();
    for (size_t w = 0; w < width; ++w) { if (table[0][w] == '+') cols.push_back(w); }
    for (size_t h = 0; h < height; ++h) { if (table[h][0] == '+') rows.push_back(h); }
    for (size_t h = rows[coords[1][0]] + 1; h < rows[coords[0][0] + 1]; ++h) {
        for (size_t w = cols[coords[0][1]] + 1; w < cols[coords[1][1] + 1]; ++w) {
            if (table[h][w] == '|' || table[h][w] == '-' || table[h][w] == '+')
                table[h][w] = ' ';
        }
    }
    if (coords[0][1] == 0) {
        for (size_t h = rows[coords[1][0]] + 1; h < rows[coords[0][0] + 1]; ++h) {
            if (table[h][0] == '+') table[h][0] = '|';
        }
    }
    if (coords[1][0] == 0) {
        for (size_t w = cols[coords[0][1]] + 1; w < cols[coords[1][1] + 1]; ++w) {
            if (table[0][w] == '+') table[0][w] = '-';
        }
    }
    if (coords[0][0] == rows.size() - 2) {
        for (size_t w = cols[coords[0][1]] + 1; w < cols[coords[1][1] + 1]; ++w) {
            if (table[height - 1][w] == '+') table[height - 1][w] = '-';
        }
    }
    if (coords[1][1] == cols.size() - 2) {
        for (size_t h = rows[coords[1][0]] + 1; h < rows[coords[0][0] + 1]; ++h) {
            if (table[h][width  - 1] == '+') table[h][width  - 1] = '|';
        }
    }
    return table;
}
