#!/usr/bin/node

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const req = require('request');

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      req(characters[i], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    };
  }
});
