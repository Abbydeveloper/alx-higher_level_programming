#!/usr/bin/node
u
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint(c) {
    let squareChar = c;

    if (c === undefined) {
      squareChar = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(squareChar.repeat(this.width));
    }
  }
}

module.exports = Square;
