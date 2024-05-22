#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req(url, function (error, response, body) {
  if (error)
    console.log(error);
  else {
    const films_list = JSON.parse(body).results;
    let characters = [];

    for (const film of films_list) {
      characters = characters.concat(film.characters);
    }
    const count = characters.filter( function (character) {
      return (character.includes('18'));
    });

    console.log(count.length);
  }
});
