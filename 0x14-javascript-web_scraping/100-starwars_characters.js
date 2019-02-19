#!/usr/bin/node
const request = require('request');

const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let characters = JSON.parse(body)['characters'];
    for (let character of characters) {
      request(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body)['name']);
        }
      });
    }
  }
});
