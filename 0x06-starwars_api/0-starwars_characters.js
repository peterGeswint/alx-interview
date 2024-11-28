#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Movie not found');
    return;
  }
  const characters = JSON.parse(body).characters;

  const fetchCharacter = (url, index) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      console.log(JSON.parse(body).name);
      if (index < characters.length - 1) {
        fetchCharacter(characters[index + 1], index + 1);
      }
    });
  };

  if (characters.length > 0) {
    fetchCharacter(characters[0], 0);
  }
});
