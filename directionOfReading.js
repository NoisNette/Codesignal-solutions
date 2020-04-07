function directionOfReading(numbers) {
    let strArr = numbers.map(x=>'0'.repeat(numbers.length - x.toString().length) + x)
  let finalnumbers = []
  for(let i=0;i<strArr.length;i++){
    for(let j=0;j<strArr[i].length;j++){
      finalnumbers[j]? finalnumbers[j] += strArr[i][j] : finalnumbers[j] = strArr[i][j]
    }
  }
  return finalnumbers.map(x=>+x)
}
