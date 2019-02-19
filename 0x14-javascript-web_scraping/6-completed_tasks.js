#!/usr/bin/node
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET',
  headers: {
    'content-type': 'application/json'
  }
};
request(options, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    let completedTasks = {};
    let json = JSON.parse(data);
    for (let i = 0; i < json.length; i++) {
      if (!(json[i].userId in completedTasks)) {
        completedTasks[json[i].userId] = 0;
      }
      if (json[i].completed) {
        completedTasks[json[i].userId]++;
      }
    }
    console.log(completedTasks);
  }
});
