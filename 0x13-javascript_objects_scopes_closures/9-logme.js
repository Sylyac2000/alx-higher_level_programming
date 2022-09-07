#!/usr/bin/node

let cpt = -1;
module.exports.logMe = function (item) {
  cpt++;
  console.log(cpt + ': ' + item);
};
