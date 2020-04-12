int lateRide(int n) {
    int h1 = 0;
    int h2 = 0;
    int m1 = 0;
    int m2 = 0;
    int mins = n % 60;

    if (n / 60 < 10) h2 = floor(n / 60);
    if (n / 60 == 10) h1 = 1;

    if (n / 60 > 10 & n / 60 < 20) {
        h1 = 1;
        h2 = floor(n / 60) - 10;
    }
    if (n / 60 == 20) h1 = 2;   
    if (n / 60 > 20) {
        h1 = 2;
        h2 = floor(n / 60) - 20;
    }

    if (mins != 0) {
        m1 = floor(mins / 10);
        m2 = mins % 10;
    }
    return h1 + h2 + m1 + m2;
}
