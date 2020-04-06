bool isInformationConsistent(vector<vector<int>> evidences) {
    using namespace std;
    int m = evidences.size(), n = evidences[0].size();
    for (int j = 0; j < n; j++) {
        set<int> nums;
        for (int i = 0; i < m; i++) {
            int num = evidences[i][j];
            if (num != 0) {
                nums.insert(num);
            }
        }
        if (nums.size() > 1) {
            return false;
        }
    }
    return true;
}
