#!/usr/bin/node

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const req = require('request');

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    console.log(characters);
    characters.forEach(function (character, index, arr) {
      req(arr[index], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
