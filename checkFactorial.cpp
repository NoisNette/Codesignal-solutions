bool checkFactorial(int n) {
    using namespace std;
    vector<long long> facts{1};
    for (long long i = 2; i <= 20; i++) {
        facts.push_back(facts[facts.size() - 1] * i);
    }
    for (auto fact: facts) {
        if (n == fact) {
            return true;
        }
    }
    return false;
}
