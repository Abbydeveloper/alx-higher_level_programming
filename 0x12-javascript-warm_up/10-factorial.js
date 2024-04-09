#!/usr/bin/node

const a = process.argv[2];

function factorial (x) {
  if (x < 0) {
    return (-1);
  } else if (x === 0 || isNaN(x)) {
    return (1);
  }
  return (x * factorial(x - 1));
}
console.log(factorial(Number(a)));
