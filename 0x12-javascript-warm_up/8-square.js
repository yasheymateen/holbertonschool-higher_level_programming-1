#!/usr/bin/node
if (process.argv[2] && Number(process.argv[2])) {
  let size = Number(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let val = '';
    for (let j = 0; j < size; j++) {
      val += 'X';
    }
    console.log(val);
  }
} else {
  console.log('Missing size');
}
