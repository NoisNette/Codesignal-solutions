int divisors(int n) {
    int middle = floor(sqrt(n));
    int res = 0;
    for (int factor = 1; factor <= middle; factor++) {
        if (n % factor == 0) {
            res += 2;
        }
    }
    if (middle * middle == n) {
        res--;
    }
    return res;
}

int divNumber(int k, int l, int r) {
    int res = 0;
    for (int n = l; n <= r; n++) {
        if (divisors(n) == k) {
            res++;
        }
    }
    return res;
}
