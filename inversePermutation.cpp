vector<int> inversePermutation(vector<int> permutation) {
    using namespace std;
    vector<int> result(permutation.size());
    for (int i = 0; i < permutation.size(); i++) {
        result[permutation[i] - 1] = i + 1;
    }
    return result;
}
