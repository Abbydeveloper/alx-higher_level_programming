#!/usr/bin/node

const data = require('./101-data').dict;

const newDict = {};

for (const [key, value] of Object.entries(data)) {
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}

console.log(newDict);
