#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const data = process.argv[3];
fs.writeFile(filePath, data, function (err, data) {
  if (err) {
    console.log(err);
  }
});
