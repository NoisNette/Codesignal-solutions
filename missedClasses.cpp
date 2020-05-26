int missedClasses(int year, vector<int> daysOfTheWeek, vector<string> holidays) {
    using namespace std;
    set<int> cache;
    for (auto num: daysOfTheWeek) {
        cache.insert(num % 7);
    }
    int res = 0;
    for (auto holiday: holidays) {
        string time = to_string(year) + "-" + holiday + " 00:00:00";
        tm date;
        stringstream ss(time);
        ss >> get_time(&date, "%Y-%m-%d %H:%M:%S");
        mktime(&date);
        if (date.tm_mon < 8) {
            date.tm_year++;
            mktime(&date);
        }
        int wday = date.tm_wday;
        if (cache.find(wday) != cache.end()) {
            res++;
        }
    }
    return res;
}
