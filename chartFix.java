int chartFix(int[] chart) {
    int[] DP = new int[chart.length];
    int maxLength = 1;
    DP[0] = 1;

    for (int i = 1; i < chart.length; i++) {
        DP[i] = 1;

        for (int j = i - 1; j >= 0; j--)
            if (DP[j] + 1 > DP[i] && chart[j] < chart[i]) {
                DP[i] = DP[j] + 1;
            }

        if (DP[i] > maxLength) {
            maxLength = DP[i];
        }
    }

    return chart.length - maxLength;
}
