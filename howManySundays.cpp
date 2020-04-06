int howManySundays(int n, string startDay) {
    using namespace std;
    vector<string> days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    int a = distance(days.begin(), find(days.begin(), days.end(), startDay));
    int b = a + n;
    int a1 = a / 7;
    int b1 = b / 7;
    return b1 - a1;
}
