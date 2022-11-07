const n = require("fs").readFileSync("input.txt").toString().split("\n");

let fib = [];
for (let i = 0; i <= n; i++) {
  if (i < 1) {
    fib[0] = 0;
  } else if (0 < i < 2) {
    fib[1] = 1;
  }
  if (2 <= i) {
    let num = fib[i - 1] + fib[i - 2];
    fib[i] = num;
  }
}
console.log(fib[fib.length - 1]);

//푸는중
//여러줄 받는 코드가 아니라 하나의 입력만 받는 코드로 고치니까 풀림
//solved!!
