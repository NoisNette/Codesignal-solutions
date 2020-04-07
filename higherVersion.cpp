vector<int> split(string ver) {
    using namespace std;
    vector<int> res;
    int idx = 0;
    while (true) {
        int dot_idx = ver.find('.', idx);
        if (dot_idx != string::npos) {
            res.push_back(stoi(ver.substr(idx, dot_idx - idx)));
        } else {
            res.push_back(stoi(ver.substr(idx)));
            break;
        }
        idx = dot_idx + 1;
    }
    return res;
}

bool higherVersion(string ver1, string ver2) {
    using namespace std;
    vector<int> nums1 = split(ver1), nums2 = split(ver2);
    return nums1 > nums2;
}
