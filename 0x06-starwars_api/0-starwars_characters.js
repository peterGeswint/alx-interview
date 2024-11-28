#!/usr/bin/python3
"""
This script prints all characters of a Star Wars movie in the same order
as they appear in the "characters" list in the /films/ endpoint.
"""

import requests
import sys

def get_characters(movie_id):
    """
    Retrieves and prints all characters of the specified Star Wars movie.
    
    Args:
        movie_id (int): The ID of the Star Wars movie.
    """
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Movie not found")
        return
    
    movie_data = response.json()
    characters = movie_data.get("characters", [])
    
    for character_url in characters:
        character_response = requests.get(character_url)
        if character_response.status_code == 200:
            character_data = character_response.json()
            print(character_data.get("name"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-starwars_characters.py <Movie ID>")
    else:
        try:
            movie_id = int(sys.argv[1])
            get_characters(movie_id)
        except ValueError:
            print("Movie ID must be an integer")
