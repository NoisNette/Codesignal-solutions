int deleteDigit(int n) {
    using namespace std;
    string item = to_string(n);
    for (int i = 1; i < item.size(); i++) {
        if (item[i - 1] < item[i]) {
            return stoi(item.substr(0, i - 1) + item.substr(i));
        }
    }
    return stoi(item.substr(0, item.size() - 1));
}
