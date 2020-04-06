String chessNotation(String notation) {
    char[][] board = new char[8][8];
    String resultNotation = "";
    int col=7, row=0;
    for(char ch: notation.toCharArray()) {
        if(ch!='/') {	
            if(Character.isAlphabetic(ch)) {	
                board[row++][col] = ch;
            }
            else {
                for(int j=0; j<ch-'0'; j++) {
                    board[row++][col] = '1';
                }
            }
        }
        else {	
            col--;
            row=0;
        }
    }
    Stack<Character> stack = new Stack<Character>();
    char position;
    int number=0;
    for(int i=0; i<8; i++) {
        for(int j=0; j<8; j++) {
            position = board[i][j];
            if(Character.isAlphabetic(position)) {
                stack.push(position);
            }
            else {
                number = Character.getNumericValue(position);
                if(!stack.isEmpty()) {
                    char temp = stack.pop();
                    if(Character.isDigit(temp)) {
                        number += Character.getNumericValue(temp);					
                        stack.push((char)(number+'0'));
                    }
                    else {
                        stack.push(temp);
                        stack.push((char)(number+'0'));
                    }
                }
                else {
                    stack.push((char)(number+'0'));
                }
            }
        }
        if(i<7) stack.push('/');
    }
    while(!stack.isEmpty()) {	
        resultNotation += stack.pop();
    }
    return new StringBuffer(resultNotation).reverse().toString();
}
