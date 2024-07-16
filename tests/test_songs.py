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
    
    assert response.len == 2
    assert response[0].name == "Song 1"
    assert response[1].name == "Song 2"
