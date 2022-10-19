#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', function (error, content) {
  console.log(error || content);
});
