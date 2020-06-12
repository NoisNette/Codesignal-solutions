int bfsComponentSize(vector<vector<bool>> matrix) {
    using namespace std;
    vector<int> nodes{1};
    set<int> visited;
    while (!nodes.empty()) {
        vector<int> next_level;
        for (auto node: nodes) {
            visited.insert(node);
            for (int j = 0; j < matrix.size(); j++) {
                if (matrix[node][j]) {
                    if (visited.find(j) == visited.end()) {
                        next_level.push_back(j);
                    }
                }
            }
        }
        nodes = next_level;
    }
    return visited.size();
}
