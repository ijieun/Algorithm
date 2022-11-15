// const input = require("fs")
//   .readFileSync(__dirname + "/input.txt")
//   .toString()
//   .split("\n")
//   .map(Number);
const fs = require("fs");
const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const Total = input.reduce((r, v) => {
  return r + v;
}, 0);
let answer = "";
for (var i = 0; i < 9; i++) {
  if (answer.length > 0) break;
  for (let j = i + 1; j < 9; j++) {
    if (Total - input[i] - input[j] == 100) {
      const truth = input
        .filter((_, k) => k != i && k != j)
        .sort((a, b) => a - b);
      answer = truth.join("\n");
      console.log(answer);
      break;
    }
  }
}
//read&solved
