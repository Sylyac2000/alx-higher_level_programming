#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];
request(url, function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body).results;
    console.log(films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
