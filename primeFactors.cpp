vector<int> primeFactors(int n) {
    using namespace std;
    vector<int> res;
    int p = 1;
    while (p <= sqrt(n)) {
        if (p != 1) {
            while (n % p == 0) {
                res.push_back(p);
                n /= p;
            }
        }
        p++;
    }
    if (n > 1) {
        res.push_back(n);
    }
    return res;
}
