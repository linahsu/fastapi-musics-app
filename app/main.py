from fastapi import FastAPI
from random import choice

from app.models import SongLibrary, Song, SongInDb

app = FastAPI(title="Music Library API", description="API for managing music library", version="0.1.1")

@app.post("/songs", response_model=dict | str, status_code=201)
def add_song(song: Song):
  """Adds a new song to the collection"""
  return SongLibrary.add_song(song)

@app.get("/songs", response_model=list[SongInDb])
def get_all_songs():
  """Get all songs in the collection as a list of Songs"""
  return SongLibrary.get_all_songs()
  
@app.get("/songs/random", response_model=SongInDb)
def get_random_song():
  """Get a random song from the collection"""
  all_songs = SongLibrary.get_all_songs()
  return choice(all_songs)
  
@app.get("/songs/{song_id}", response_model=dict | SongInDb)
def get_song_by_id(song_id: str):
  """Get a song by ID"""
  try:
    return SongLibrary.get_song_by_id(song_id)
  except ValueError:
    return "Song not found", 404
  
@app.put("/songs/{song_id}", response_model=dict | str)
def update_song(song_id: str, song: Song):
  """Update a song"""
  try:
    return SongLibrary.update_song(song_id, song)
  except ValueError:
    return "Song not found", 404
  
@app.delete("/songs/{song_id}")
def delete_song(song_id: str):
  ...