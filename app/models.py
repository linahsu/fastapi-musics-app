from pydantic import BaseModel, Field
from app.database import db

class Song(BaseModel):
  name: str
  artist: str
  album: str
  release_year: int
  genre: str
  image: str
  
class SongInDb(Song):
  id: str = Field(alias="_id")
  
class SongLibrary:
  _collection = db["songs"]
  
  @classmethod
  def add_song(cls, song: Song):
    cls._collection.insert_one(song.__dict__)
    return "Song added successfully"
  
  @classmethod
  def get_all_songs(cls):
     return [
       SongInDb(_id=str(song.pop("_id")), **song)
       for song
       in cls._collection.find()
     ]