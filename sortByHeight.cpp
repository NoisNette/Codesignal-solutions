std::vector<int> sortByHeight(std::vector<int> a) {
    std::vector<int> b(a.begin(), a.end());
    std::sort(b.begin(), b.end());
    b.erase(std::remove(b.begin(), b.end(), -1), b.end());
    int idx = 0;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != -1) {
            a[i] = b[idx++];
        }
    }
    return a;
}
