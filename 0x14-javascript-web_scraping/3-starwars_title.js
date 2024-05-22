#!/usr/bin/node

const req = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

req(url, function (error, httpResponse, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
