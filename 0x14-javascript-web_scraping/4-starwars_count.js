#!/usr/bin/node
const request = require('request');

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
  } else if (response.statusCode === 200) {
    let json = JSON.parse(body);

    const movies = json.results;
    let count = 0;
    for (let i = 0; i < movies.length; i++) {
      let movie = movies[i];
      for (let j = 0; j < movie.characters.length; j++) {
        let character = movie.characters[j];
        if (character.indexOf('18/') > -1) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
