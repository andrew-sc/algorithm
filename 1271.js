var fs = require('fs');
var inputData = fs.readFileSync(0, 'utf8').toString().split(' ');
var m = BigInt(inputData[0]);
var n = BigInt(inputData[1]);
var result = (m / n);
console.log(result);
var remainder = (m % n);
console.log(remainder);

// 뭐가 맞는것인가!!!!!!!!