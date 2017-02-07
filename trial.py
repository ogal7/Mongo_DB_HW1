import csv

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


for item in li:
        print str(item) + "\n\n"