from pymongo import MongoClient

server = MongoClient('127.0.0.1')
db = server.modusoperandi
collection = db['students']
d = {}
li = [d]