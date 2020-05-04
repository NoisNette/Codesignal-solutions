vector<string> bishopDiagonal(string bishop1, string bishop2) {
    using namespace std;
    int x1 = bishop1[0] - 'a', y1 = bishop1[1] - '1';
    int x2 = bishop2[0] - 'a', y2 = bishop2[1] - '1';
    if (abs(x1 - x2) == abs(y1 - y2)) {
        int dx = x1 < x2 ? -1 : 1;
        int dy = y1 < y2 ? -1 : 1;
        while (true) {
            int x = x1 + dx, y = y1 + dy;
            if (x < 0 || x >= 8 || y < 0 || y >= 8) {
                break;
            }
            x1 = x;
            y1 = y;
        }
        dx *= -1;
        dy *= -1;
        while (true) {
            int x = x2 + dx, y = y2 + dy;
            if (x < 0 || x >= 8 || y < 0 || y >= 8) {
                break;
            }
            x2 = x;
            y2 = y;
        }
    }
    string s1 = {x1 + 'a', y1 + '1'};
    string s2 = {x2 + 'a', y2 + '1'};
    vector<string> res{s1, s2};
    sort(res.begin(), res.end());
    return res;
}
