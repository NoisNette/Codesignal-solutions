int differentValues(std::vector<int> a, int d) {
    int n = a.size();
    int best = -1;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int diff = abs(a[i] - a[j]);
            if (diff <= d) {
                if (best == -1) {
                    best = diff;
                } else {
                    best = max(best, diff);
                }
                if (best == d) {
                    break;
                }
            }
        }
    }
    return best;
}
