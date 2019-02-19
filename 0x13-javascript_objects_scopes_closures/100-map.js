#!/usr/bin/node
const l1 = require('./100-data.js').list;
console.log(l1);
let index = 0;
const l2 = l1.map(function multByIndex (x) {
  return x * index++;
});
console.log(l2);
