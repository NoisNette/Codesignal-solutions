function textJustification(words, L) {
    let lines = [], index = 0;
    
    while(index < words.length) {
        let count = words[index].length;
        let last = index + 1;
        
        while(last < words.length) {
            if (words[last].length + count + 1 > L) break;
            count += words[last].length + 1;
            last++;
        }
        
        let line = "";
        let difference = last - index - 1;

        if (last === words.length || difference === 0) {
            for (let i = index; i < last; i++) {
                line += words[i] + " ";
            }
            
            line = line.substr(0, line.length - 1);
            for (let i = line.length; i < L; i++) {
                line += " ";
            }
        } else {

            let spaces = (L - count) / difference;
            let remainder = (L - count) % difference;
            
            for (let i = index; i < last; i++) {
                line += words[i];
                
                if( i < last - 1) {
                    let limit = spaces + ((i - index) < remainder ? 1 : 0)
                    for (let j = 0; j <= limit; j++) {
                        line += " ";
                    }
                }
            }
        }
        lines.push(line);
        index = last;
    }
    return lines;
}
