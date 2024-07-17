import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import SongLibrary

@pytest.fixture(autouse=True, scope="module")
def reset_database():
  SongLibrary._collection.delete_many({})
  yield
  SongLibrary._collection.delete_many({})
  

@pytest.fixture
def client():
  return TestClient(app)


def test_add_song(client):
  song1 = {
    "name": "Song 1",
    "artist": "Artist 1",
    "album": "Album 1",
    "release_year": 2021,
    "genre": "Pop",
    "image": "https://example.com/image1.jpg"
  }
  
  response = client.post("/songs", json=song1)
  
  assert response.status_code == 201
  assert response.json() == "Song added successfully"


def test_get_all_songs(client):
    song2 = {
    "name": "Song 2",
    "artist": "Artist 2",
    "album": "Album 2",
    "release_year": 2012,
    "genre": "Rock",
    "image": "https://example.com/image2.jpg"
  }
    client.post("/songs", json=song2)
    
    response = client.get("/songs")
    
    assert len(response.json()) == 2
    assert type(response.json()[0]) is dict
    assert response.json()[0]["name"] == "Song 1"
    assert response.json()[1]["name"] == "Song 2"
    for song in response.json():
      assert "name" in song
      assert "artist" in song
      assert "album" in song
      assert "release_year" in song
      assert "genre" in song
      assert "image" in song


def test_get_random_song(client):
  response = client.get("/songs/random")
  
  assert type(response.json()) is dict
  assert "name" in response.json()
  assert "artist" in response.json()
  assert "album" in response.json()
  assert "release_year" in response.json()
  assert "genre" in response.json()
  assert "image" in response.json()
  

def test_get_song_by_id(client):
  song_id = str(SongLibrary.get_all_songs()[0].id)
  
  response = client.get(f"/songs/{song_id}")
  
  assert type(response.json()) is dict
  assert response.json()["name"] == "Song 1"


def test_update_song(client):
  song3 = {
    "name": "Song 3",
    "artist": "Artist 3",
    "album": "Album 3",
    "release_year": 2019,
    "genre": "Soul",
    "image": "https://example.com/image3.jpg"
  }
  
  song_id = str(SongLibrary.get_all_songs()[0].id)
  response = client.put(f"/songs/{song_id}", json=song3)
  
  updated_song = SongLibrary.get_song_by_id(song_id)
  
  assert response.json() == "Song updated"
  assert updated_song.name == "Song 3"
  assert updated_song.artist == "Artist 3"
  assert updated_song.album == "Album 3"
  assert updated_song.release_year == 2019
  assert updated_song.genre == "Soul"
  assert updated_song.image == "https://example.com/image3.jpg"
  

def test_delete_song():
  ...