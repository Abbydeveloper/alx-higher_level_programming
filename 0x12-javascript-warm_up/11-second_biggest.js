#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const a = process.argv.slice(2).map(Number);
  const sortedArr = a.sort((x, y) => {return (y - x)});
  console.log(sortedArr[1])
}
