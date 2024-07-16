from pymongo import MongoClient
import os

client = MongoClient('mongodb://localhost:27017/')

db = client[os.getenv("DB_TEST", 'songs_db')]