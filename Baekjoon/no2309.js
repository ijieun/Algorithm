const input = require("fs")
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(Number);
console.log(input);

var arr;
for (var i = 0; i < 8; i++) {
  for (var j = i + 1; j < 9; j++) {
    if (
      input.reduce((sum, item) => sum + item, 0) ===
      input[i] + input[j] + 100
    ) {
      arr = input.filter((item) => item !== input[i] && input !== input[j]);
      break;
    }
  }
  if (!!arr) break;
}

arr.sort((a, b) => a - b);
for (var i = 0; i < 7; i++) {
  console.log(arr[i]);
}
