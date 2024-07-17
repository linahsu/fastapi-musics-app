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

@pytest.fixture
def song_id():
  return str(SongLibrary.get_all_songs()[0].id)