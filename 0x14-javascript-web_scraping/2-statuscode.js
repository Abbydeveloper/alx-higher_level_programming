#!/usr/bin/node
const req = require('request');
const file = process.argv[2];

req(file, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
