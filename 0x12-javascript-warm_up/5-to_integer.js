#!/usr/bin/node

const a = process.argv[2];

if (isNaN(a) || a === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(a));
}
