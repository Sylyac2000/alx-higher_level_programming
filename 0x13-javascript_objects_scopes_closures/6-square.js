#!/usr/bin/node

const BaseCarre = require('./5-square');

module.exports = class Square extends BaseCarre {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
