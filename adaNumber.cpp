bool adaNumber(string line) {
    using namespace std;
    string tmp;
    regex_replace(back_inserter(tmp), line.begin(), line.end(), regex("_"), "");
    line = tmp;
    regex reg1("^[\\d]+$");
    smatch matches;
    regex_search(line, matches, reg1);
    if (matches.size() > 0) return true;
    regex reg2("^([\\d]+)#([\\da-fA-F]+)#$");
    regex_search(line, matches, reg2);
    if (matches.size() > 0) {
        string part1 = matches[1].str();
        string part2 = matches[2].str();
        regex reg3("^\\d+$");
        regex_search(part1, matches, reg3);
        if (matches.size() == 0 || part1.size() > 2) {
            return false;
        }
        int base = stoi(part1);
        if (base <= 1 || base > 16) return false;
        vector<string> bases = {"", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "aA", "bB", "cC", "dD", "eE", "fF"};
        string extra_bases = "";
        for (int i = 1; i <= base; i++) {
            extra_bases += bases[i];
        }
        regex reg4("^[" + extra_bases + "]+$");
        regex_search(part2, matches, reg4);
        if (matches.size() > 0) return true;
    }
    return false;
}
