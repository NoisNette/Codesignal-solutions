int increasingNumber(int x, int n) {
    int y, z;
    for (int i = 1; i <= n; i++){
        y = 0;
        do {
    		z = x + y;
    		y++;
		}while(z % i != 0);
        x = z;        
    }
	return z;
}
