from pydantic import BaseModel, Field
from pymongo import ReturnDocument
from app.database import db
from bson import ObjectId

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
    
  @classmethod
  def get_song_by_id(cls, song_id: str):
    song = cls._collection.find_one({ "_id": ObjectId(song_id) })
    
    if song:
      return SongInDb(_id=str(song.pop("_id")), **song)
    else:
      raise ValueError("Song not found")
    
  @classmethod
  def update_song(cls, song_id: str, song: Song):
    updated_song = cls._collection.find_one_and_update(
      { "_id": ObjectId(song_id) },
      { "$set": song.__dict__ },
      return_document=ReturnDocument.AFTER,
    )
    
    if updated_song is None:
      raise ValueError("Song not found")
    
    return "Song updated"