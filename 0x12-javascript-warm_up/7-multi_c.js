#!/usr/bin/node

const args = parseInt(process.argv[2]);

if (isNaN(args)) {
  console.log('Missing number of occurences');
} else {
  for (let i = args; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
