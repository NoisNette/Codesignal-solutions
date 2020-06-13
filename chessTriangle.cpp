int chessTriangle(int n, int m) {
    using namespace std;
    vector<vector<int>> steps;
    for (auto dx: vector<int>{-2, -1, 1, 2}) {
        for (auto dy: vector<int>{-2, -1, 1, 2}) {
            if (abs(dx) + abs(dy) != 3) continue;
            vector<int> step1 = {dx, dy};
            for (auto ddx: vector<int>{-2, -1, 1, 2}) {
                for (auto ddy: vector<int>{-abs(ddx), abs(ddx)}) {
                    if (ddx == dx || ddy == dy) {
                        step1.push_back(ddx);
                        step1.push_back(ddy);
                    }
                }
            }
            vector<int> step2 = {dx, dy};
            for (int ddy = -3; ddy <= 3; ddy++) {
                if (abs(0 - dx) == abs(ddy - dy)) {
                    step2.push_back(0);
                    step2.push_back(ddy);
                }
            }
            for (int ddx = -3; ddx <= 3; ddx++) {
                if (abs(ddx - dx) == abs(0 - dy)) {
                    step2.push_back(ddx);
                    step2.push_back(0);
                }
            }
            steps.push_back(step1);
            steps.push_back(step2);
        }
    }
    int res = 0;
    for (int x = 0; x < m; x++) {
        for (int y = 0; y < n; y++) {
            for (auto step: steps) {
                int x1 = x + step[0], y1 = y + step[1];
                if (x1 < 0 || x1 >= m || y1 < 0 || y1 >= n) continue;
                for (int i = 1; i < step.size() / 2; i++) {
                    x1 = x + step[2 * i];
                    y1 = y + step[2 * i + 1];
                    if (x1 < 0 || x1 >= m || y1 < 0 || y1 >= n) continue;
                    res++;
                }
            }
        }
    }
    return res;
}
