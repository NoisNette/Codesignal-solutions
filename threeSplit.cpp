int threeSplit(std::vector<int> a) {
    long long sum = 0;
    for (auto num: a) {
        sum += num;
    }
    sum /= 3;
    int res = 0;
    long long s1 = 0;
    for (int i = 0; i < a.size(); i++) {
        s1 += a[i];
        if (s1 == sum) {
            long long s2 = 0;
            for (int j = i + 1; j < a.size(); j++) {
                s2 += a[j];
                if (s2 == sum) {
                    if (j < a.size() - 1) {
                        res++;
                    }
                }
            }
        }
    }
    return res;
}
