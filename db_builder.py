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
teachersCollection = db['teachers']
d = {}
teacherLi = [d]
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




#teachersCollection.remove({})




with open('teachers.csv') as teachersfile:
        reader = csv.reader(teachersfile)
        for row in reader:
                xx = False
                for dic in teacherLi:
                        if 'teacher' in dic and dic['teacher'] == row[1]: #if this teacher already has a document
                                dic[row[0]] = row[2]
                                xx = True
                if xx == False:#we have to make a new dic/doc for this teacher
                        newDic = {}
                        newDic['teacher'] = row[1]
                        newDic[row[0]] = row[2]
                        newDic['students'] = []
                        teacherLi.append(newDic)


classesList = ['softdev', 'ceramics', 'systems', 'greatbooks']


nastyWoman = collection.find()
for boss in nastyWoman:#each boss is a student document object
        if 'id' in boss:
                studentId = boss['id']
                for k in boss: #k is a student attribute, in this case it shud be a class
                        if k in classesList:
                                for teacher in teacherLi: #teacher document object
                                        for key in teacher:
                                                if key == k: #if this teacher teaches the class I want to enter
                                                        if 'students' in teacher:
                                                                print "hi"
                                                                print studentId
                                                                print teacher['students']
                                                                teacher['students'].append(studentId)





#teachersCollection.remove({})
for item in teacherLi:
       teachersCollection.insert_one(item)


#Each teacher document should contain their name, class, period and students in that class
#The student data should be a list of ids that match the ids of students from the other collection.






#for item in teacherLi:
#       teachersCollection.insert_one(item)

#for dictionary in li:
#	collection.insert_one(dictionary)




cursor = collection.find()
for itemA in cursor:
    print str(itemA) + "\n"


print "\n\n\n"


cursor1 = teachersCollection.find()
for itemB in cursor1:
    print itemB
    print "\n"

##Add a document: create a dictionary(document) **for each student**

