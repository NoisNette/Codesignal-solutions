int countSumOfTwoRepresentations(int n, int l, int r) {
    using namespace std;
    int a = max(l, n - r), b = min(r, n - l);
    return a <= b ? (a + b) / 2 - a + 1 : 0;
}
