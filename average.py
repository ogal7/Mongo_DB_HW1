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
    counter = 1.0
    for course in classes:
    	if course in student:
	        gradeSum += int(student[course])
	        counter += 1
    avg = gradeSum/counter
    student['average'] = avg
    if 'name' in student and 'id' in student:
        print "Name:"+student["name"] +"\nID:"+student["id"]+ "\nAverage:"+str(student["average"]) +"\n"
