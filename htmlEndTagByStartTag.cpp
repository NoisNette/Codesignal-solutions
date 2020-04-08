string htmlEndTagByStartTag(string startTag) {
    using namespace std;
    int pos = 0;
    while (++pos < startTag.length()) {
        if (startTag[pos] == '>' || startTag[pos] == ' ') {
            break;
        }
    }
    string res = startTag.substr(0, pos) + ">";
    res.insert(1, "/");
    return res;
}
