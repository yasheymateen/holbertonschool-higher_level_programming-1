#!/usr/bin/node
const dict = require('./101-data').dict;
const occurences = {};
for (let key in dict) {
  if (dict[key] in occurences) {
    occurences[dict[key]].push(key);
  } else {
    occurences[dict[key]] = [];
    occurences[dict[key]].push(key);
  }
}
console.log(occurences);
