const input = require("fs").readFileSync("input.txt").toString().split("\n");
const count = Number(input[0]);
const nums = input[1].split(" ").map(Number);

let max = nums[0];
let min = nums[0];

for (let i = 0; i < count; i++) {
  if (max < nums[i]) {
    max = nums[i];
  }
  if (min > nums[i]) {
    min = nums[i];
  }
}
console.log(min, max);

//https://www.acmicpc.net/problem/10818
//https://pstudio411.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EB%B0%B1%EC%A4%80%EC%9D%84-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-%EC%9C%84%ED%95%9C-nodejs-%EB%9F%B0%ED%83%80%EC%9E%84-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0
//solved!!
