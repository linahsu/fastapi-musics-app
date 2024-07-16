from fastapi import FastAPI

app = FastAPI(title="Music Library API", description="API for managing music library", version="0.1.1")

@app.post("/songs")
def add_song():
  ...

@app.get("/songs")
def get_all_songs():
  ...
  
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