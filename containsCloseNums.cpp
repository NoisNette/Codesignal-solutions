bool containsCloseNums(vector<int> nums, int k) {
    using namespace std;
    map<int, int> cache;
    for (int i = 0; i < nums.size(); i++) {
        int num = nums[i];
        if (cache.find(num) == cache.end()) {
            cache[num] = i;
        } else {
            int j = cache[num];
            if (i - j <= k) {
                return true;
            }
            cache[num] = i;
        }
    }
    return false;
}
