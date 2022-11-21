const input = require("fs")
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(Number);
var sum = 0;
var h = [];
for (var i = 0; i < input.length; i++) {
  if (input[i] % 2 == 1) {
    sum = sum + input[i];
    h.push(input[i]);
  }
}
if (h.length == 0) {
  console.log(-1);
} else {
  console.log(sum);
  console.log(Math.min(...h));
}
//solved!!!
//sort함수 사용X
//Math.min.apply() 사용O
//Spread Operator 사용O
