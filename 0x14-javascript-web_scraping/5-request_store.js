#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    const filePath = process.argv[3];
    fs.writeFile(filePath, data, function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
