bool isSumOfConsecutive(int n) {
    for (int i = 0; i < n; i++){
        int sum = 0;
        for (int j = i; j < n; j++){
            sum += j;
            if (sum == n) return true;
            else if (sum > n) break;
        }
    }
    return false;
}
