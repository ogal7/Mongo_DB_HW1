from pymongo import MongoClient
import csv

coursesfile = open('courses.csv','r')
peepsfile = open('peeps.csv','r')

server = MongoClient('149.89.150.100')
db = server.modusoperandi
col = db['students']

