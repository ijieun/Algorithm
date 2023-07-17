// const fs = require("fs");
// const inputData = fs.readFileSync(0, "utf8").toString().split(" ");

const inputData = [240, 20];
const L = [];

const N = parseInt(inputData[0]);
const K = parseInt(inputData[1]);

for (var i = 0; i < N + 1; i++) {
  if (N % i == 0) {
    L.push(i);
  }
}
if (L.length < K) {
  console.log(0);
} else {
  console.log(L[K - 1]);
}
