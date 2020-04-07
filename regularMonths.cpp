string regularMonths(string currMonth) {
    using namespace std;
    tm date;
    stringstream ss("01-" + currMonth + " 00:00:00");
    ss >> get_time(&date, "%d-%m-%Y %H:%M:%S");
    while (true) {
        if (date.tm_mon == 11) {
            date.tm_year++;
            date.tm_mon = 0;
        } else {
            date.tm_mon++;
        }
        mktime(&date);
        if (date.tm_wday == 1) {
            break;
        }
    }
    ss.str("");
    ss.clear();
    ss << put_time(&date, "%m-%Y");
    return ss.str();
}
