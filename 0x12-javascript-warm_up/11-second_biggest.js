#!/usr/bin/node

const array = process.argv.slice(2);

if (array.length < 2) {
  console.log(0);
} else {
  array.sort((x, y) => x - y);
  array.pop();
  console.log(array.pop());
}
