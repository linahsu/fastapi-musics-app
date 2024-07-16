from fastapi import FastAPI

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
  
@app.get("/songs/random")
def get_random_song():
  ...
  
@app.get("/songs/{song_id}")
def get_song_by_id(song_id: str):
  ...
  
@app.put("/songs/{song_id}")
def update_song(song_id: str):
  ...
  
@app.delete("/songs/{song_id}")
def delete_song(song_id: str):
  ...