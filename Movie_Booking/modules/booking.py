import json
import os

FILMS_FILE = 'Movie_Booking/data/films.json'

def list_films():
    if not os.path.exists(FILMS_FILE):
        print(f"⚠️ File {FILMS_FILE} tidak ditemukan!")  # Debug
        return []
    with open(FILMS_FILE, 'r') as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            print("❌ Format JSON films.json error!")
            return []

def tampilkan_films():
    films = list_films()
    if not films:
        print("Belum ada film yang tersedia.")
        return

    print("\n=== Daftar Film ===")
    for film in films:
        print(f"{film['id']}. {film['judul']}")
        print("   Jadwal: ", ", ".join(film['jadwal']))
