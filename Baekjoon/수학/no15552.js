let input = require("fs").readFileSync("input.txt").toString().split("\n");
let count = Number(input[0]);
let answerStr = "";

for (let i = 1; i <= count; i++) {
  let num = input[i].split(" ");
  console.log(num);
  answerStr += Number(num[0]) + Number(num[1]) + "\n";
}

console.log(answerStr);
