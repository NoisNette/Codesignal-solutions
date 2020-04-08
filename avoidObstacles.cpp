int avoidObstacles(vector<int> inputArray) {
    using namespace std;
    for (int step = 2; ; step++) {
        bool valid = true;
        for (auto num: inputArray) {
            if (num % step == 0) {
                valid = false;
                break;
            }
        }
        if (valid) {
            return step;
        }
    }
    return -1;
}
