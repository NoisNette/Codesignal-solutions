int gcd(int a, int b) {
    if (a % b == 0) {
        return b;
    }
    return gcd(b, a % b);
}

vector<int> get_factors(int n) {
    using namespace std;
    vector<int> factors;
    int f = 2;
    while (n % f == 0) {
        factors.push_back(f);
        n /= f;
    }
    f++;
    while (f <= sqrt(n)) {
        while (n % f == 0) {
            factors.push_back(f);
            n /= f;
        }
        f += 2;
    }
    if (n > 1) {
        factors.push_back(n);
    }
    return factors;
}

int greatestCommonPrimeDivisor(int a, int b) {
    using namespace std;
    int g = gcd(max(a, b), min(a, b));
    if (g == 1) {
        return -1;
    }
    auto factors = get_factors(g);
    return factors.back();
}
