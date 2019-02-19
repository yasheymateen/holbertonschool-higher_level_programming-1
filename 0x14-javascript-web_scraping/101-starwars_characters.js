#!/usr/bin/node
const request = require('request');

let people = [];
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    people = JSON.parse(body)['characters'];
    printInOrder(people, 0);
  }
});

function printInOrder (urls, index) {
  if (urls[index] !== undefined) {
    request(urls[index], function (err, response, body) {
      if (err) {
        console.log(err);
      } else {
        process.stdout.write(JSON.parse(body)['name'] + '\n');
        printInOrder(urls, index + 1);
      }
    });
  }
}
