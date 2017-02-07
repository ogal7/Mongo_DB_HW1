from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')
db = server.modusoperandi
collection = db['students']
classes = ['systems', 'softdev', 'ceramics', 'greatbooks']

cursor = collection.find()
for student in cursor:
    avg = 0
    for course in classes:
        avg += student[course]
    dict = {'average': avg}
    student['average'] = avg
    print student['average']
