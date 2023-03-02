# mongodb测试

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import bson

# 连接mongodb的test数据库
mongo_url = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000"
client = MongoClient(mongo_url)
db = client.test
collectionName = "post"
# serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)

# 删除所有数据
ids = db[collectionName].delete_many({})

db[collectionName].create_index("id", unique=True)


for num in range(1, 20):
    post = {
        "id": bson.int64.Int64(num),
        "name": "Post-" + str(num),
        "content": "学习mongodb"
    }

    # 写入数据
    db[collectionName].insert_one(post)

pprint("find first post:")
# 查询数据
firstPost = db.post.find_one({'id': 1})
pprint(firstPost)

pprint("\nfind all posts:")
posts = db.post.find({})
for post in posts:
    pprint(post)
