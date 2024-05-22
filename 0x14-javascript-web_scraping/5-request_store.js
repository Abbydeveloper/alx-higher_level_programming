#!/usr/bin/node

const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const path = process.argv[3];

req(url, function (error, response, body) {
  if (error) {
    console.log(error)
  } else {
    fs.writeFile(path, body, 'utf-8', function (err) {
      if (error) {
        console.log(err)
      }
    });
  }
});
