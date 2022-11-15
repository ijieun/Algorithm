const input = require("fs")
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");
//   .map(Number);
console.log(input[0].substring(0));
console.log(input);
