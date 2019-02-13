#!/usr/bin/node
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  const phrase = 'C is fun';
  const times = process.argv[2];
  for (let i = 0; i < times; i++) {
    console.log(phrase);
  }
}
