import pymongo
from pymongo import MongoClient

cluster = MongoClient("client = pymongo.MongoClient("mongodb+srv://kido5327:<1b0ff61b0ff6>@cluster0.axhlqmd.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"] 

post1 = ("_id":5, "name":"joe")
post2 = ("_id":6, "name":"bill")

collection.replace_one({"_id":5}, {"name":"testing"})
post_count = collection.count_documents({})
print(post_count)








