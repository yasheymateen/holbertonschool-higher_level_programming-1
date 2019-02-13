#!/usr/bin/node

const argument = Number(process.argv[2]);
console.log(factorial(argument));

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
