bool whoseTurn(std::string p) {
    string ori = "b1;g1;b8;g8";
    int d1 = p[0] - ori[0] +
        p[1] - ori[1] +
        p[3] - ori[3] +
        p[4] - ori[4];
    int d2 = p[6] - ori[6] +
        p[7] - ori[7] +
        p[9] - ori[9] +
        p[10] - ori[10];
    return (d1 - d2) % 2 == 0;
}
