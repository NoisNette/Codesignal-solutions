bool containsNearbyAlmostDuplicate(std::vector<int> nums, int k, int t) {
    set <long long> st;
    int n = nums.size();
    long long tt = t;
    map <long long, int> mp;
    for(int i = 0; i < n; ++i) {
        if(st.empty()) {
            st.insert(nums[i]);
            mp[nums[i]]++;
            continue;
        }
        long long x = nums[i];
        if(i - k - 1 >= 0) {
            mp[nums[i - k - 1]]--;
            if(mp[nums[i - k - 1]] == 0) {
                st.erase(nums[i - k - 1]);
            }
        }
        auto it = st.lower_bound(nums[i]);
        if(it != st.end()) {
        if(abs((*it) - x) <= tt) 
            return true;
        }
        if(it != st.begin()) {
            --it;
            if(abs((*it) - x) <= tt) 
            return true;
        }
            st.insert(nums[i]);
            mp[nums[i]]++;
        }
    return false;
}
