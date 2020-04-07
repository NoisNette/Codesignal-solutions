vector<int> subtractionByRegrouping(int minuend, int subtrahend) {
    using namespace std;
    vector<int> res;
    while (minuend > 0) {
        int d1 = minuend % 10;
        minuend /= 10;
        int d2 = subtrahend % 10;
        subtrahend /= 10;
        if (d1 >= d2) {
            res.push_back(d1);
        } else {
            minuend--;
            res.push_back(d1 + 10);
        }
    }
    return res;
}
