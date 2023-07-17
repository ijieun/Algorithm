const input = require("fs")
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n");

//   .map(Number);
// console.log(input[0].substring(0));
console.log(input);
for (let i = 0; i < input.length; i++) {
  let text = input[i];
  let count = 0;
  let searchChar = "0";
  let pos = text.indexOf(searchChar);
  // console.log(text);

  while (pos !== -1) {
    count++;
    pos = text.indexOf(searchChar, pos + 1);
  }
  if (count == 0) {
    console.log("E");
  } else if (count == 1) {
    console.log("A");
  } else if (count == 2) {
    console.log("B");
  } else if (count == 3) {
    console.log("C");
  } else if (count == 4) {
    console.log("D");
  }
}
//read&solved
