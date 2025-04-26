import json
import os

FILMS_FILE = 'data/films.json'

def list_films():
    if not os.path.exists(FILMS_FILE):
        return []
    with open(FILMS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
