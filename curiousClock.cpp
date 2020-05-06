time_t strtot(string str) {
    using namespace std;
    tm date;
    stringstream ss(str + ":00");
    ss >> get_time(&date, "%Y-%m-%d %H:%M:%S");
    auto time = mktime(&date);
    return time;
}

string curiousClock(string someTime, string leavingTime) {
    using namespace std;
    auto time1 = strtot(someTime);
    auto time2 = strtot(leavingTime);
    auto time3 = time1 - (time2 - time1);
    
    char cache[100];
    tm *date = localtime(&time3);
    strftime(cache, 100, "%Y-%m-%d %H:%M", date);

    string res{cache};
    return res;
}
