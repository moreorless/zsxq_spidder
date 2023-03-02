# mongodb测试

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# 连接mongodb的test数据库
mongo_url = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000"
client = MongoClient(mongo_url)
db = client.test

print("find first post:")
# 查询数据
firstPost = db.post.find_one({'id': 1})
pprint(firstPost)

print("find all posts:")
posts = db.post.find({'id': 1})
pprint(len([posts]))

# find ids
print("\nfind all ids:")
ids = db.post.distinct('id')

pprint(ids)

print("find all posts:")
posts = db.post.find({})
for post in posts:
    pprint(post)