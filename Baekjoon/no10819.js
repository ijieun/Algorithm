const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
let list = [];
let result = [];
let numbers = [];
let check = new Array(9).fill(false);
rl.on("line", function (line) {
  input.push(line);
}).on("close", async function () {
  // 답안 작성
  let answer = 0;

  numbers = input[1].split(" ").sort((a, b) => a - b);
  let n = input[0];
  re(0, n, 0);
  //console.log(result.join('\n'));
  console.log(max_abs());
  process.exit();
});

let max_abs = function () {
  let max = 0;
  result.reduce((acc, cur) => {
    let tmp = cur.split(" ");
    let sum = 0;
    for (let i = 0; i < tmp.length - 1; i++) {
      sum += Math.abs(tmp[i] * 1 - tmp[i + 1] * 1);
    }
    max = Math.max(max, sum);
  }, "");
  return max;
};

let re = function (cnt, n, start) {
  if (cnt == n) {
    result.push(list.join(" "));
    return;
  }
  for (let i = start; i < n; i++) {
    if (!check[i]) {
      check[i] = true;
      list[cnt] = numbers[i];
      re(cnt + 1, n, 0);
      check[i] = false;
    }
  }
};
