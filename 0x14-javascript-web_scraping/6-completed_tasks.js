#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let completedTasks = {};
    let json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed) {
        if (!(json[i].userId in completedTasks)) {
          completedTasks[json[i].userId] = 1;
        } else {
          completedTasks[json[i].userId]++;
        }
      }
    }
    console.log(completedTasks);
  }
});
