bool decipher(string cipher, string &plain) {
    using namespace std;
    if (cipher.size() == 0) {
        return true;
    }
    for (int i = 0; i < cipher.size(); i++) {
        string head = cipher.substr(0, i + 1);
        string tail = cipher.substr(i + 1);
        if (head.size() > 3) {
            break;
        }
        int h = stoi(head);
        if (!('a' <= h && h <= 'z')) {
            continue;
        }
        plain += char(h);
        if (decipher(tail, plain)) {
            return true;
        }
        plain = plain.substr(0, plain.size() - 1);
    }
    return false;
}

string decipher(string cipher) {
    using namespace std;
    string res = "";
    decipher(cipher, res);
    return res;
}
