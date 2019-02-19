#!/usr/bin/node
const request = require('request');

const character = 'https://swapi.co/api/people/18/';
const options = {
  url: process.argv[2],
  method: 'GET',
  headers: {
    'content-type': 'application/json'
  }
};

request(options, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response === 200) {
    let json = JSON.parse(body);

    const movies = json.results;
    let count = 0;
    for (let i = 0; i < movies.length; i++) {
      if (movies[i].characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
});
