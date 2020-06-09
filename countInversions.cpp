#define M 1000000007
int countInversions(std::vector<int> a) {
    int res = 0;
    
    std::vector<int> temp;
    for(int i = a.size() - 1; i >= 0; i--)
    {
        std::vector<int>::iterator it = std::lower_bound(temp.begin(), temp.end(), a[i]);
        res += (int)(it - temp.begin()) % M;
        res %= M;
        temp.insert(it, a[i]);
    }
    
    return res % M;
}
