#!/usr/bin/node

const a = process.argv[2];

function factorial(x) {
  if (x < 0) {
    return (-1);
  } else if (isNaN(a) || a === undefined) {
    return (1);
  }
  return (x * factorial(x - 1));
}
console.log(factorial(a));
