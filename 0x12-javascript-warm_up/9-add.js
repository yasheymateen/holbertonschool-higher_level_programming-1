#!/usr/bin/node

if (!process.argv[2] || !process.argv[3]) {
  console.log('NaN');
} else {
  console.log(add(Number(process.argv[2]), Number(process.argv[3])));
}

function add (a, b) {
  return a + b;
}
