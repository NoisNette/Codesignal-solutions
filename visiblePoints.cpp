int visiblePoints(std::vector<std::vector<int>> points) {
    const double pi = M_PI, pi_45 = M_PI_4, pi_360 = M_PI*2.0;
    const double epsilon = 1e-10;
    int n = points.size(), result = 0;
    vector<double> angles(n);
    for (int i = 0; i < n; i++){
        double angle = atan2(points[i][1], points[i][0]);
        angles[i] = angle;
        if (angle < pi_45-pi){
            angles.push_back(angle + pi_360);
        }
    }
    sort(angles.begin(), angles.end());
    for (auto it = angles.begin(); it != angles.begin()+n; ++it){
        auto bound = upper_bound(it, angles.end(), *it+(pi_45+epsilon));
        int curr = distance(it, bound);
        if (curr > result){
            result = curr;
        }
    }
    return result;
}
