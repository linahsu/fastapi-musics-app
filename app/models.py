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