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
  song = {
    "name": "Song 1",
    "artist": "Artist 1",
    "album": "Album 1",
    "release_year": 2021,
    "genre": "Pop",
    "image": "https://example.com/image.jpg"
  }
  response = client.post("/songs", json=song)
  assert response.status_code == 201
  assert response.json() == "Song added successfully"
