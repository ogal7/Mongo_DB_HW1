from pymongo import MongoClient

server = MongoClient('149.89.150.100')
db = server.modusoperandi
col = db['students']
