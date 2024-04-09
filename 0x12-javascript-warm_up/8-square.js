#!/usr/bin/node

const a = process.argv[2];

if (isNaN(a) || a === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    console.log('X'.repeat(a));
  }
}
