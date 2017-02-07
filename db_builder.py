from pymongo import MongoClient
import csv


##RELEVANT NOTES
# databases 
# _________________

# Collections 
# ______________

# Documents 
# _____________

#{
#id:
#name:
#age:
#courses,marks:	
#}


#coursesfile = open('courses.csv','r')
#peepsfile = open('peeps.csv','r')

server = MongoClient('127.0.0.1')
db = server.modusoperandi
collection = db['students']
d = {}
li = [d]


with open('courses.csv') as coursesfile:
        reader = csv.reader(coursesfile)
        for row in reader: #each row is a list
        	idnum = row[2]
        	x = False
        	for dic in li:
        		if 'id' in dic and dic['id'] == idnum:
        			dic[row[0]] = row[1]
        			x = True
        	if x == False: ##create a new dictionary for that student
        		di = {'id': idnum}
        		di[row[0]] = row[1]
                        li.append(di)


with open('peeps.csv') as peepsfile:
        reader = csv.reader(peepsfile)
        for row in reader:
        	idnumA = row[2]
        	for dic in li: 
        		if 'id' in dic and dic['id'] == idnumA:
        			dic['name'] = row[0]
        			dic['age'] = row[1]

#for dictionary in li:
#	collection.insert_one(dictionary)

collection.remove({})



#cursor = collection.find()
#for item in cursor:
#        print item



##Add a document: create a dictionary(document) **for each student**

