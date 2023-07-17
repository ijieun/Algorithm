// 10진수를 2진수로 변환하기

// const fs = require("fs");
// const inputData = fs.readFileSync(0, "utf8").toString().split(" ");

// const inputData = [2, 3];

// const A = parseInt(inputData[0]);
// const B = parseInt(inputData[1]);

var A = 150;
const array = [];
while (A > 1) {
  array.push(Math.floor(A % 2));

  A = A / 2;
}

console.log(array.reverse());
