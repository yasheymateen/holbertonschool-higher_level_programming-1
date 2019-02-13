#!/usr/bin/node
if (!process.argv[3]) {
  console.log('0');
} else {
  let largest;
  let secondLargest;

  if (Number(process.argv[2]) > Number(process.argv[3])) {
    largest = Number(process.argv[2]);
    secondLargest = Number(process.argv[3]);
  } else {
    largest = Number(process.argv[3]);
    secondLargest = Number(process.argv[2]);
  }

  let i = 4;
  while (process.argv[i]) {
    let num = Number(process.argv[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (largest > num && num > secondLargest) {
      secondLargest = num;
    }
    i++;
  }

  console.log(secondLargest);
}
