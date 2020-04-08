function stringPermutations(str){
    var array = getPermutations(str);
    array = removeDuplicates(array);
    return array.sort();
}

removeDuplicates = array =>array.filter((item,index) => array.indexOf(item) == index)

function getPermutations(str){
    var permutations = [],
        nextWord = [],    
        chars = []
    ;
    if (typeof str === 'string') chars = str.split(''); 
    else if (typeof str === 'number') {
      str = str + ""; 
      chars = str.split('');
    }
    permutate(chars);
    return permutations;
    function permutate(chars){ 
        if(chars.length === 0)permutations.push(nextWord.join(''));            
        for (var i=0; i < chars.length; i++){ 
            chars.push(chars.shift());
            nextWord.push(chars[0]);     
            permutate(chars.slice(1)); 
            nextWord.pop();           
        }
    }
}
