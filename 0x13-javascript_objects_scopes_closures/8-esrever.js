#!/usr/bin/node
module.exports.esrever = function (list) {
  const reverse = [];
  let len = list.length - 1;
  while (len >= 0) {
    reverse.push(list[len]);
    len--;
  }
  return reverse;
};
