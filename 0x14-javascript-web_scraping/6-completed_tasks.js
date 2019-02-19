#!/usr/bin/node
const request = require('request');

const options = {
  url: process.argv[2]
};
request.get(options, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let completedTasks = {};
    let json = JSON.parse(body);
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
