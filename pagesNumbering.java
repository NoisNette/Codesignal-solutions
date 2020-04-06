int pagesNumbering(int n) {
    int tenPower = 1, digitsPerPage = 1, result = 0;
        while (tenPower <= n) {
            result += tenPower * 9 * digitsPerPage;
            tenPower *= 10;
            digitsPerPage++;
        }
        result += (n - tenPower + 1) * (digitsPerPage - 1);
        return result;
}
