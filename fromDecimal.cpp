string fromDecimal(int b, int n) {
    using namespace std;
    if (n == 0) {
        return "0";
    }
    string res = "";
    while (n > 0) {
        int digit = n % b;
        res = to_string(digit) + res;
        n /= b;
    }
    return res;
}
