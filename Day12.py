{
    "firstname": "AAA",
    "lastname": "BBB",
    "age": 25,
    "languages_known":["python","java","c"],
    "mark":{"mark1":87,"mark2":98,"mark3":78},
    "cgpa":8.4,
    "graduated":"True",
    "percentage":84
},
{
    
    "firstname": "CCC",
    "lastname": "DDD",
    "age": 23,
    "languages_known":["python","java","c"],
    "mark":{"mark1":95,"mark2":100,"mark3":88},
    "cgpa":9.0,
    "graduated":"True",
    "percentage":90
}
}
import json 
from pymongo import MongoClient 
myclient = MongoClient("mongodb://localhost:27017/") 
db = myclient["GFG"] 
Collection = db["data"] 
with open('data.json') as file: 
	file_data = json.load(file) 
if isinstance(file_data, list): 
	Collection.insert_many(file_data) 
else: 
	Collection.insert_one(file_data) 
