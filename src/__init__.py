from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

#mongodb 호출
client = MongoClient('localhost', 27017)
db = client['dshobby']

post_coll = db['post']  #content collection