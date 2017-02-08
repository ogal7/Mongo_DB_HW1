from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')
db = server.modusoperandi
collection = db['students']
classes = ['systems', 'softdev', 'ceramics', 'greatbooks']

#print collection.count()
#cursor1 = collection.find()
#for i in cursor1:
#	print i
#	if "name" in i:
#		print i["name"]

cursor = collection.find()
for student in cursor:
    gradeSum = 0.0
    counter = 0.0
    for course in classes:
	if course in student:
		avg += student[course]
		counter += 1
    avg = gradeSum/counter
    dict = {'average': avg}
    student['average'] = avg
    print "Name: "+student["name"] + "\nID: "+student["id"] + "\nAverage: " + student['average']
