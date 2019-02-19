#!/usr/bin/node
const request = require('request');

const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET',
  headers: {
    'content-type': 'application/json'
  }
};
request(options, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let json = JSON.parse(body);
    console.log(json.title);
  }
});
