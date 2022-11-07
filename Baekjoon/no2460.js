const input = require("fs").readFileSync("input.txt").toString().split("\n");

let people = 0;
let max_people = 0;
let train = [];

for (let i = 0; i < input.length; i++) {
  train.push(input[i].split(" ").map(Number));
}

for (let i = 0; i < input.length; i++) {
  people = people - train[i][0];
  people = people + train[i][1];
  if (people > max_people) {
    max_people = people;
  }
}
console.log(max_people);
//solved!!!
