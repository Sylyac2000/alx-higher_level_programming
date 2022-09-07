#!/usr/bin/node

module.exports.esrever = function (list) {
  const tablo = [];

  for (let i = list.length - 1; i >= 0; i--) {
    tablo.push(list[i]);
  }
  return tablo;
};
