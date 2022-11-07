// const fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString();
// console.log(input);
// input = input.split("\n");
// console.log(input);

// const testCaseNum = +input[0];
// console.log("testCaseNum: ", testCaseNum);
// for (let i = 1; i <= testCaseNum; ++i) {
//   const arr = input[i].split(" ");
//   let newArr = [];
//   for (let i = 0; i < arr.length; ++i) {
//     newArr.push(+arr[i]);
//   }
//   console.log("arr: ", arr);
//   console.log("newarr: ", newArr);
//   break;
// }

const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const count = Number(input[0]);
const nums = input[1].split(" ").map(Number);

//https://covenant.tistory.com/224
//백준 브론즈 문제 추천
