#!/usr/bin/node

const a = process.argv[2];

if (isNaN(a) || a === undefined) {
  console.log(1);
} else {
  let b = 1;
  for (let i = 1; i <= a; i++) {
    b *= i;
  }
  console.log(b);
}
