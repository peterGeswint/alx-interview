#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// The URL of the Star Wars API for the given movie
const url = `https://swapi.dev/api/films/${movieId}/`;

// Send a GET request to the API
request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
    return;
  }

  // Parse the response body to a JavaScript object
  const movieData = JSON.parse(body);

  // Iterate over the "characters" array and print each character's name
  movieData.characters.forEach(function (characterUrl) {
    // For each character URL, send a GET request to get the character's data
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.log('Error:', error);
        return;
      }

      // Parse the character's data and print the character's name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
