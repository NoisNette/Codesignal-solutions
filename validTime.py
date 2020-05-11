bool validTime(string time) {
    using namespace std;
    regex reg("^(\\d\\d):(\\d\\d)$");
    smatch matches;
    regex_search(time, matches, reg);
    if (matches.size() != 3) {
        return false;
    }
    int h = stoi(matches[1].str());
    int m = stoi(matches[2].str());
    return 0 <= h && h <= 23 && 0 <= m && m <= 59;
}
